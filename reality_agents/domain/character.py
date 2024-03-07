from typing import Dict
from reality_agents.domain.emotion import EmotionalState

# eventually Dict[str, str] for personality


class Character:
    def __init__(
        self, name: str, pronouns: str, personality: str, relationship_to_target: str
    ):
        self.name: str = name
        self.pronouns: str = pronouns
        self.personality: str = personality
        self.emotional_state: Dict[str, int] = EmotionalState()
        self.relationship_to_target = relationship_to_target

    def initialize_state(self, situation: str, relationship_to_target: str):
        self.emotional_state.initialize_emotional_state(
            self.personality, situation, relationship_to_target
        )
