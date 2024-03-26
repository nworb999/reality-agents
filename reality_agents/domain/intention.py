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

    def initialize_objective(self, emotional_state, conflict, relationship_to_target):
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
                conflict=conflict,
                relationship_to_target=relationship_to_target,
                emotional_state=emotional_state,
            )
            raw_response = get_response(prompt=prompt)
            formatted_response = parse_initial_objective(raw_response)
            self.objective = formatted_response["objective"]
            self.tactics = formatted_response["tactics"]
            print(formatted_response["objective"])
            retries += 1

        # and first intention as a bullet point

    def initialize_intention(self, emotional_state):
        prompt = format_init_intention_prompt(
            objective=self.objective,
            persona=self.persona,
            tactics=self.tactics,
            emotional_state=emotional_state,
        )
        self.intention = parse_init_intention(get_response(prompt))
        print("INTENTION", self.intention)

    def update_intention(self, conflict, emotional_state, convo_history):
        if self.objective == "END CONVERSATION":
            self.intention = "END CONVERSATION"
        else:
            prompt = format_update_intention_prompt(
                emotional_state=emotional_state,
                objective=self.objective,
                utterance=convo_history[-1],
            )
            self.intention = get_response(prompt)

    def is_ending_conversation(self):
        return self.intention == "END CONVERSATION"

    def get_objective(self):
        return self.objective

    def get_intention(self):
        return self.intention

    def _is_objective_fulfilled(self, conflict, emotional_state, convo_history):
        prompt = format_is_objective_fulfilled_prompt(
            objective=self.objective,
            persona=self.persona,
            conflict=conflict,
            emotional_state=emotional_state,
            convo_history=convo_history,
        )
        response = get_response(prompt)
        return starts_with_yes(response) == "Yes"
