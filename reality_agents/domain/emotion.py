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

    def initialize_emotional_state(self, persona, situation, relationship_to_target):
        prompt = format_emotion_init_prompt(persona, situation, relationship_to_target)
        response = parse_emotion_response(get_response(prompt))
        for key, value in response.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def update_emotional_state_from_utterance(self, utterance):
        prompt = format_emotion_update_prompt(utterance, self.__str__())
        while True:
            try:
                response = parse_emotion_response(get_response(prompt))
                for key, value in response.items():
                    if hasattr(self, key.lower()):
                        clamped_value = clamp(value, 1, 5)
                        setattr(self, key.lower(), clamped_value)
                break  # Exit the loop once the update is successful
            except Exception as e:
                print(f"Error updating emotions: {e}. Retrying...")

    def get_emotion(self, emotion):
        return self.__dict__.get(emotion, "Invalid emotion")

    def __str__(self):
        return (
            f"Happiness: {self.happiness}, Sadness: {self.sadness}, Anxiety: {self.anxiety}, "
            f"Anger: {self.anger}, Fear: {self.fear}, Boredom: {self.boredom}"
        )
