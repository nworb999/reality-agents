from reality_agents.domain.emotion import EmotionalState
from reality_agents.domain.intention import Intention
from typing import Dict, List

from reality_agents.domain.memory import Memory

# balances personality, emotional state, and conversation utterances with memory (eventually)

# move initialize + everything before utterance prompt in here, including emotional step and intention step


class Psyche:
    def __init__(self, personality: str, relationship_to_target: str):
        self.personality = personality
        self.emotional_state = EmotionalState()
        self.intention = Intention(persona=personality)
        self.relationship_to_target = relationship_to_target
        self.memory = Memory()

    def update_memory(self, conflict, utterance=None):
        self.memory.update_memory(
            conflict=conflict,
            personality=self.personality,
            objective=self.get_objective(),
            emotional_state=self.emotional_state,
            utterance=utterance,
            relationship_to_target=self.relationship_to_target,
        )

    def get_memory(self):
        return self.memory.get_memory()

    def initialize_state(
        self, conflict: str, scene: str, relationship_to_target: str, utterance: str
    ):
        self._initialize_emotional_state(conflict, relationship_to_target, utterance)
        self._initialize_intention_and_objective(
            conflict=conflict, scene=scene, utterance=utterance
        )

    def update_state(self, conflict: str, utterance):
        self.update_emotional_state(utterance)
        self.update_intention(utterance)
        self.update_memory(conflict=conflict, utterance=utterance)

    def get_emotional_state(self):
        return self.emotional_state.get()

    def _initialize_emotional_state(
        self, conflict: str, relationship_to_target: str, utterance: str
    ):
        self.emotional_state.initialize(
            self.personality, conflict, relationship_to_target, utterance
        )

    def update_emotional_state(self, utterance: str):
        self.emotional_state.update(utterance)

    def get_intention(self):
        return self.intention.get_intention()

    def _initialize_intention_and_objective(self, conflict: str, scene, utterance):
        emotional_state = self.get_emotional_state()
        self.intention.initialize_objective(
            scene=scene,
            emotional_state=emotional_state,
            conflict=conflict,
            relationship_to_target=self.relationship_to_target,
        )

        self.intention.initialize_intention(emotional_state, utterance)

    def update_intention(self, utterance: str):
        emotional_state = self.get_emotional_state()
        self.intention.update_intention(
            emotional_state=emotional_state, memory=self.memory, utterance=utterance
        )

    def get_objective(self):
        return self.intention.get_objective()

    def is_ending_conversation(self):
        return self.intention.is_ending_conversation()
