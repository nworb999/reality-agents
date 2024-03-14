from typing import Dict, List
from reality_agents.domain.emotion import EmotionalState
from reality_agents.domain.psyche import Psyche

# eventually Dict[str, str] for personality


class Character:
    def __init__(
        self, name: str, pronouns: str, personality: str, relationship_to_target: str
    ):
        self.name: str = name
        self.pronouns: str = pronouns
        self.personality: str = personality
        self.relationship_to_target = relationship_to_target
        self.psyche: Psyche = Psyche(self.personality, self.relationship_to_target)

    def initialize_psyche(self, conflict: str, relationship_to_target: str):
        self.psyche.initialize_state(conflict, relationship_to_target)

    def update_psyche(self, conflict: str, convo_history: List[str]):
        self.psyche.update_state(convo_history=convo_history, conflict=conflict)

    def get_emotional_state(self):
        return self.psyche.get_emotional_state()

    def get_objective(self):
        return self.psyche.get_objective()

    def get_intention(self):
        return self.psyche.get_intention()

    def is_ending_conversation(self):
        return self.psyche.is_ending_conversation()
