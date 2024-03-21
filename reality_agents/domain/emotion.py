from reality_agents.services.llm.prompt_injection import (
    format_emotion_init_prompt,
    format_emotion_update_prompt,
)
from reality_agents.services.llm.ollama_handler import get_response
from utils.string import parse_emotion_response
from utils.statistics import clamp


class EmotionalState:
    def __init__(self):
        self.happiness = 1
        self.sadness = 1
        self.anxiety = 1
        self.anger = 1
        self.fear = 1
        self.boredom = 1

    def process_emotion_response(self, prompt, max_retries=1, update=False):
        for _ in range(max_retries):
            try:
                response = parse_emotion_response(get_response(prompt))
                self._update_attributes(response, update)
                break
            except SyntaxError:
                return
            except Exception:
                return

    def _update_attributes(self, response, update):
        for key, value in response.items():
            attr_name = key.lower() if hasattr(self, key.lower()) else key
            if update:
                value = clamp(value, 1, 5)
            setattr(self, attr_name, value)

    def initialize_emotional_state(self, persona, conflict, relationship_to_target):
        prompt = format_emotion_init_prompt(persona, conflict, relationship_to_target)
        self.process_emotion_response(prompt)

    def update_emotional_state_from_utterance(self, utterance):
        prompt = format_emotion_update_prompt(utterance, self.get())
        max_retries = 3
        self.process_emotion_response(prompt, max_retries, update=True)

    def get(self):
        return (
            f"Happiness: {self.happiness}, Sadness: {self.sadness}, Anxiety: {self.anxiety}, "
            f"Anger: {self.anger}, Fear: {self.fear}, Boredom: {self.boredom}"
        )
