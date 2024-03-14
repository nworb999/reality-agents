from reality_agents.services.llm.ollama_handler import get_response
from reality_agents.services.llm.prompt_injection import (
    format_init_intention_prompt,
    format_objective_init_prompt,
    format_should_update_objective_prompt,
    format_update_objective_prompt,
    format_update_intention_prompt,
    format_is_objective_fulfilled_prompt,
)


def check_response(sentence):
    if sentence.strip().lower().startswith("yes"):
        return "Yes"
    elif sentence.strip().lower().startswith("no"):
        return "No"
    else:
        return "The sentence does not start with Yes or No."


# add an excalidraw diagram for all these objects
# objective as less dynamic, intention as next-line specific
class Intention:
    def __init__(self, persona):
        self.persona: str = persona
        self.objective: str
        self.intention: str

    def initialize_objective(self, emotional_state, conflict, relationship_to_target):
        prompt = format_objective_init_prompt(
            self.persona, conflict, relationship_to_target, emotional_state
        )
        response = get_response(prompt)
        self.objective = response
        pass

    def update_objective(self, conflict, emotional_state, convo_history):
        is_objective_fulfilled_prompt = format_is_objective_fulfilled_prompt(
            self.get_objective(), self.persona, conflict, emotional_state, convo_history
        )
        is_objective_fulfilled_response = get_response(is_objective_fulfilled_prompt)
        answer_done = check_response(is_objective_fulfilled_response)
        if answer_done == "yes":
            self.objective = "END CONVERSATION"
        should_update_prompt = format_should_update_objective_prompt(
            self.get_objective(),
            self.persona,
            conflict,
            emotional_state,
            convo_history=convo_history,
        )
        response = get_response(should_update_prompt)
        answer = check_response(response)
        if answer == "yes":
            update_prompt = format_update_objective_prompt(
                self.get_objective(),
                conflict,
                self.persona,
                emotional_state,
                convo_history,
            )
            update_response = get_response(update_prompt)
            print(update_response)
            self.objective = update_response
        return

    def initialize_intention(self, conflict, emotional_state):
        prompt = format_init_intention_prompt(
            self.get_objective(), self.persona, conflict, emotional_state
        )
        response = get_response(prompt)
        self.intention = response
        return

    def update_intention(self, conflict, emotional_state, convo_history):
        if self.objective == "END CONVERSATION":
            self.intention = "END CONVERSATION"
        else:
            prompt = format_update_intention_prompt(
                emotional_state=emotional_state,
                objective=self.get_objective(),
                utterance=convo_history[-1],
            )
            response = get_response(prompt)
            self.intention = response
        return

    def is_ending_conversation(self):
        if self.intention == "END CONVERSATION":
            return True
        else:
            return False

    def get_objective(self):
        return self.objective

    def get_intention(self):
        return self.intention
