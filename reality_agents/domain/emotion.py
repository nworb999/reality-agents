from reality_agents.services.llm.prompt_injection import (
    format_emotion_init_prompt,
    format_emotion_update_prompt,
)
from reality_agents.services.llm.ollama_handler import get_response
from utils.string import parse_emotion_response


class EmotionalState:
    def __init__(self):
        self.emotional_state = "neutral"
        self.max_retries = 3

    def initialize(self, persona, conflict, relationship_to_target, utterance=None):
        retries = 0
        while retries < self.max_retries:
            prompt = format_emotion_init_prompt(
                persona, conflict, relationship_to_target, utterance
            )
            response = parse_emotion_response(get_response(prompt))
            if response:
                self.emotional_state = response
                break
            retries += 1

    def update(self, utterance):
        retries = 0
        while retries < self.max_retries:
            prompt = format_emotion_update_prompt(utterance=utterance, state=self.get())
            response = parse_emotion_response(get_response(prompt))
            if response:
                self.emotional_state = response
                break
            retries += 1

    def get(self):
        return self.emotional_state
