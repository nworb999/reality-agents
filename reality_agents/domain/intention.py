from reality_agents.services.llm.ollama_handler import get_response
from reality_agents.services.llm.prompt_injection import (
    format_init_intention_prompt,
    format_objective_init_prompt,
    format_should_update_objective_prompt,
    format_update_objective_prompt,
    format_update_intention_prompt,
    format_is_objective_fulfilled_prompt,
)
from utils.string import starts_with_yes


# objective as less dynamic, intention as next-line specific
class Intention:
    def __init__(self, persona):
        self.persona = persona
        self.objective = None
        self.intention = None

    def initialize_objective(self, emotional_state, conflict, relationship_to_target):
        prompt = format_objective_init_prompt(
            self.persona, conflict, relationship_to_target, emotional_state
        )
        self.objective = get_response(prompt)

    def update_objective(self, conflict, emotional_state, convo_history):
        if self._is_objective_fulfilled(conflict, emotional_state, convo_history):
            self.objective = "END CONVERSATION"
        elif self._should_update_objective(conflict, emotional_state, convo_history):
            self._perform_objective_update(conflict, emotional_state, convo_history)

    def _is_objective_fulfilled(self, conflict, emotional_state, convo_history):
        prompt = format_is_objective_fulfilled_prompt(
            self.objective, self.persona, conflict, emotional_state, convo_history
        )
        response = get_response(prompt)
        return starts_with_yes(response) == "Yes"

    def _should_update_objective(self, conflict, emotional_state, convo_history):
        prompt = format_should_update_objective_prompt(
            self.objective, self.persona, conflict, emotional_state, convo_history
        )
        response = get_response(prompt)
        return starts_with_yes(response) == "Yes"

    def _perform_objective_update(self, conflict, emotional_state, convo_history):
        prompt = format_update_objective_prompt(
            self.objective, conflict, self.persona, emotional_state, convo_history
        )
        self.objective = get_response(prompt)

    def initialize_intention(self, conflict, emotional_state):
        prompt = format_init_intention_prompt(
            self.objective, self.persona, conflict, emotional_state
        )
        self.intention = get_response(prompt)

    def update_intention(self, conflict, emotional_state, convo_history):
        if self.objective == "END CONVERSATION":
            self.intention = "END CONVERSATION"
        else:
            prompt = format_update_intention_prompt(
                emotional_state, self.objective, convo_history[-1]
            )
            self.intention = get_response(prompt)

    def is_ending_conversation(self):
        return self.intention == "END CONVERSATION"

    def get_objective(self):
        return self.objective

    def get_intention(self):
        return self.intention
