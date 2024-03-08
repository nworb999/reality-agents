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

    def handle_response_errors(self, prompt, max_retries=1, update=False):
        for attempt in range(1, max_retries + 1):
            try:
                response = parse_emotion_response(get_response(prompt))
                for key, value in response.items():
                    if hasattr(self, key.lower()):
                        if update:
                            clamped_value = clamp(value, 1, 5)
                            setattr(self, key.lower(), clamped_value)
                        else:
                            setattr(self, key, value)
                break
            except SyntaxError as e:
                return
            except Exception as e:
                return
                # if attempt < max_retries:
                # print(
                #     f"Error updating emotions: {e}. Retrying... ({max_retries - attempt} attempts left)"
                # )
                # else:
                # print(
                #     f"Error updating emotions: {e}. Maximum retries reached. Moving on..."
                # )

    def initialize_emotional_state(self, persona, conflict, relationship_to_target):
        prompt = format_emotion_init_prompt(persona, conflict, relationship_to_target)
        self.handle_response_errors(prompt)

    def update_emotional_state_from_utterance(self, utterance):
        prompt = format_emotion_update_prompt(utterance, self.get())
        max_retries = 3
        self.handle_response_errors(prompt, max_retries, update=True)

    def get(self):
        return (
            f"Happiness: {self.happiness}, Sadness: {self.sadness}, Anxiety: {self.anxiety}, "
            f"Anger: {self.anger}, Fear: {self.fear}, Boredom: {self.boredom}"
        )
