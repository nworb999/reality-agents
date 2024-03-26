from reality_agents.domain.emotion import EmotionalState
from reality_agents.domain.intention import Intention
from typing import Dict, List

# balances personality, emotional state, and conversation utterances with memory (eventually)

# move initialize + everything before utterance prompt in here, including emotional step and intention step


class Psyche:
    def __init__(self, personality: str, relationship_to_target: str):
        self.personality = personality
        self.emotional_state = EmotionalState()
        self.intention = Intention(persona=personality)
        self.relationship_to_target = relationship_to_target

    def initialize_state(self, conflict: str, relationship_to_target: str):
        self._initialize_emotional_state(conflict, relationship_to_target)
        self._initialize_intention_and_objective(conflict)

    def update_state(self, conflict: str, convo_history: List[str]):
        self.update_emotional_state(convo_history[-1])
        self.update_intention(conflict, convo_history)

    def get_emotional_state(self):
        return self.emotional_state.get()

    def _initialize_emotional_state(self, conflict: str, relationship_to_target: str):
        self.emotional_state.initialize(
            self.personality, conflict, relationship_to_target
        )

    def update_emotional_state(self, utterance: str):
        self.emotional_state.update(utterance)

    def get_intention(self):
        return self.intention.get_intention()

    def _initialize_intention_and_objective(self, conflict: str):
        emotional_state = self.get_emotional_state()
        self.intention.initialize_objective(
            emotional_state, conflict, self.relationship_to_target
        )
        self.intention.initialize_intention(emotional_state)

    def update_intention(self, conflict: str, convo_history: List[str]):
        emotional_state = self.get_emotional_state()
        self.intention.update_intention(emotional_state, conflict, convo_history)

    def get_objective(self):
        return self.intention.get_objective()

    def is_ending_conversation(self):
        return self.intention.is_ending_conversation()
