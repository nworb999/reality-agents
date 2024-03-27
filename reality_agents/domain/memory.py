from reality_agents.services.llm.prompt_injection import format_convo_summary_prompt
from reality_agents.services.llm.ollama_handler import get_response
from utils.string import parse_convo_summary


class Memory:
    def __init__(self, memory=[]):
        self.memory = memory if memory else ""

    def update_memory(
        self,
        objective,
        personality,
        conflict,
        emotional_state,
        relationship_to_target,
        utterance=None,
    ):
        prompt = format_convo_summary_prompt(
            current_memory=self.memory,
            personality=personality,
            conflict=conflict,
            objective=objective,
            emotional_state=emotional_state,
            utterance=utterance,
            relationship_to_target=relationship_to_target,
        )
        self.convo_summary = parse_convo_summary(get_response(prompt))

    def get_memory(self):
        return self.memory
