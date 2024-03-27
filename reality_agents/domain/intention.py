from reality_agents.services.llm.ollama_handler import get_response
from reality_agents.services.llm.prompt_injection import (
    format_init_intention_prompt,
    format_objective_init_prompt,
    format_update_intention_prompt,
    format_is_objective_fulfilled_prompt,
)
from utils.string import starts_with_yes, parse_initial_objective, parse_init_intention


# objective as less dynamic, intention as next-line specific
class Intention:
    def __init__(self, persona):
        self.persona = persona
        self.tactics = []
        self.objective = None
        self.intention = None

    def initialize_objective(
        self, emotional_state, conflict, scene, relationship_to_target, utterance=None
    ):
        retries = 0
        max_retries = 3
        formatted_response = {}

        while (
            retries < max_retries
            and not formatted_response.get("objective")
            or not formatted_response.get("tactics")
        ):
            prompt = format_objective_init_prompt(
                persona=self.persona,
                scene=scene,
                conflict=conflict,
                relationship_to_target=relationship_to_target,
                emotional_state=emotional_state,
                utterance=utterance,
            )
            raw_response = get_response(prompt=prompt)
            formatted_response = parse_initial_objective(raw_response)
            self.objective = formatted_response["objective"]
            self.tactics = formatted_response["tactics"]
            retries += 1

    def initialize_intention(self, emotional_state, utterance=None):
        prompt = format_init_intention_prompt(
            objective=self.objective,
            persona=self.persona,
            tactics=self.tactics,
            emotional_state=emotional_state,
            utterance=utterance,
        )
        self.intention = parse_init_intention(get_response(prompt))

    def update_intention(self, memory, emotional_state, utterance):
        if self.objective == "END CONVERSATION":
            self.intention = "END CONVERSATION"
        else:
            prompt = format_update_intention_prompt(
                memory=memory,
                emotional_state=emotional_state,
                current_tactic=self.intention,
                utterance=utterance,
            )
            self.intention = get_response(prompt)

    def is_ending_conversation(self):
        return self.intention == "END CONVERSATION"

    def get_objective(self):
        return self.objective

    def get_intention(self):
        return self.intention

    def _is_objective_fulfilled(self, conflict, emotional_state, utterance):
        # move this logic up into psyche
        # use updated convo summary
        prompt = format_is_objective_fulfilled_prompt(
            objective=self.objective,
            persona=self.persona,
            conflict=conflict,
            emotional_state=emotional_state,
            utterance=utterance,
        )
        response = get_response(prompt)
        return starts_with_yes(response) == "Yes"
