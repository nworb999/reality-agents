from reality_agents.services.llm.prompt_injection import format_emotion_init_prompt
from reality_agents.services.llm.ollama_handler import get_response


# will have to init based on persona + situation + relationship to other character
class EmotionState:
    def __init__(self):
        self.happiness = 1
        self.sadness = 1
        self.anxiety = 1
        self.anger = 1
        self.fear = 1
        self.boredom = 1

    def initialize_emotion_state(persona, situation, relationship_to_target):
        prompt = format_emotion_init_prompt(persona, situation, relationship_to_target)
        response = get_response(prompt)
        print(response)

    def update_emotion(self, emotion, value):
        if emotion in self.__dict__:
            self.__dict__[emotion] = value
        else:
            print(f"{emotion} is not a valid emotion.")

    def get_emotion(self, emotion):
        return self.__dict__.get(emotion, "Invalid emotion")

    def __str__(self):
        return (
            f"Happiness: {self.happiness}, Sadness: {self.sadness}, Anxiety: {self.anxiety}, "
            f"Anger: {self.anger}, Fear: {self.fear}, Boredom: {self.boredom}"
        )
