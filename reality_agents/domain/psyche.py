from reality_agents.domain.emotion import EmotionalState
from reality_agents.domain.intention import Intention
from typing import Dict, List

# balances personality, emotional state, and conversation utterances with memory (eventually)

# move initialize + everything before utterance prompt in here, including emotional step and intention step
# initialize long-term conversational intention in here
# how would personality play into emotions updating -- make sure that is accounted
# skip emotional update on first turn


class Psyche:
    def __init__(
        self,
        personality: str,
        relationship_to_target: str,
    ):
        self.personality: str = personality
        self.emotional_state: Dict[str, int] = EmotionalState()
        # contains long-term objective and short-term intention
        self.intention: Dict[str, str] = Intention(persona=personality)
        self.relationship_to_target = relationship_to_target

    def initialize_state(self, conflict: str, relationship_to_target: str):
        self._initialize_emotional_state(conflict, relationship_to_target)
        self._initialize_objective(
            conflict=conflict, relationship_to_target=relationship_to_target
        )
        self._initialize_intention(conflict=conflict)

    def update_state(self, conflict, convo_history: List[str]):
        self.update_emotional_state(utterance=convo_history[-1])
        self.update_objective(convo_history=convo_history[:2], conflict=conflict)
        self.update_intention(convo_history=convo_history[:2], conflict=conflict)

    def get_emotional_state(self):
        return self.emotional_state.get()

    def _initialize_emotional_state(self, conflict: str, relationship_to_target: str):
        self.emotional_state.initialize_emotional_state(
            self.personality, conflict, relationship_to_target
        )

    def update_emotional_state(self, utterance: str):
        self.emotional_state.update_emotional_state_from_utterance(utterance)

    def get_intention(self):
        return self.intention.get_intention()

    def _initialize_intention(self, conflict: str):
        self.intention.initialize_intention(
            conflict=conflict,
            emotional_state=self.get_emotional_state(),
        )
        return

    def update_intention(self, convo_history: List[str], conflict: str):
        self.intention.update_intention(
            emotional_state=self.get_emotional_state(),
            convo_history=convo_history,
            conflict=conflict,
        )
        return

    def get_objective(self):
        return self.intention.get_objective()

    def _initialize_objective(self, conflict: str, relationship_to_target: str):
        self.intention.initialize_objective(
            self.get_emotional_state(),
            conflict,
            relationship_to_target,
        )
        return

    def update_objective(self, convo_history: List[str], conflict: str):
        self.intention.update_objective(
            emotional_state=self.get_emotional_state(),
            conflict=conflict,
            convo_history=convo_history,
        )
        pass

    def is_ending_conversation(self):
        return self.intention.is_ending_conversation()
