from reality_agents.domain.emotion import EmotionalState
from typing import Dict

# balances personality, emotional state, and conversation utterances with memory (eventually)

# move initialize + everything before utterance prompt in here, including emotional step and intention step
# initialize long-term conversational intention in here
# how would personality play into emotions updating -- make sure that is accounted
# skip emotional update on first turn


class Psyche:
    def __init__(
        self,
        personality: str,
        emotional_state: Dict[str, int],
        intention: Dict[str, str],
        relationship_to_target: str,
    ):
        self.personality: str = personality
        self.emotional_state: Dict[str, int] = emotional_state
        # contains long-term objective and short-term intention
        self.intention: Dict[str, str] = intention
        self.relationship_to_target = relationship_to_target

    def initialize_state(self, conflict: str, relationship_to_target: str):
        self._initialize_emotional_state(conflict, relationship_to_target)
        self._initialize_intention()
        self._initialize_objective()

    def update_state(self, utterance: str):
        self.update_emotional_state(utterance)
        self.update_objective(utterance)
        self.update_intention(utterance)

    def _initialize_emotional_state(self, conflict: str, relationship_to_target: str):
        self.emotional_state.initialize_emotional_state(
            self.personality, conflict, relationship_to_target
        )

    def update_emotional_state(self, utterance: str):
        self.emotional_state.update_emotional_state_from_utterance(utterance)

    def _initialize_intention(self, conflict: str, relationship_to_target: str):
        self.intention.initialize_intention(
            self.emotional_state, conflict, relationship_to_target
        )
        return

    def update_intention(self, utterance: str):
        self.intention.update_intention(self.emotional_state, utterance)
        return

    def _initialize_objective(self, conflict: str, relationship_to_target: str):
        self.intention.update_objective(
            self.emotional_state, conflict, relationship_to_target
        )
        pass

    def update_objective(self, utterance: str):
        self.intention.update_objective(self.emotional_state, utterance)
        pass
