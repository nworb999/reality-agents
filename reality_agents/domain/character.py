from typing import Dict
from reality_agents.domain.emotion import EmotionState

# eventually Dict[str, str] for personality


class Character:
    def __init__(self, name: str, personality: str):
        self.name: str = name
        self.personality: str = personality
        self.emotional_state: Dict[str, int] = EmotionState()

    def initialize_state(
        self, persona: str, situation: str, relationship_to_target: str
    ):
        self.emotional_state.initialize_emotion_state(
            persona, situation, relationship_to_target
        )
