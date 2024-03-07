from reality_agents.services.llm.ollama_handler import get_response
from reality_agents.services.llm.prompt_injection import format_prompt


# add an excalidraw diagram for all these objects
# objective as less dynamic, intention as next-line specific
class Intention:
    def __init__(self, objective, intention):
        self.objective = objective
        self.intention = intention

    def instantiate_objective(self, persona, conflict, relationship_to_target):
        prompt = ""
        pass

    def update_objective(self):
        # Code to update the objective property
        pass

    def instantiate_intention(self):
        # Code to instantiate the intention property
        pass

    def update_intention(self):
        # Code to update the intention property
        pass
