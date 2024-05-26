from utils.logger import logger
from reality_agents.domain.psyche import Psyche


class Character:
    def __init__(self, name: str, personality: str, relationship_to_target: str):
        self.name: str = name
        self.personality: str = personality
        self.relationship_to_target = relationship_to_target
        self.psyche: Psyche = Psyche(self.personality, self.relationship_to_target)
        self.psyche_initialized = False

    def initialize_psyche(
        self, conflict: str, scene: str, relationship_to_target: str, utterance: str
    ):
        logger.info(f"{self.name} initializing psyche...")
        self.psyche.initialize_state(
            conflict=conflict,
            relationship_to_target=relationship_to_target,
            utterance=utterance,
            scene=scene,
        )
        self.psyche_initialized = True

    def update_psyche(self, conflict: str, utterance: str):
        if self.psyche_initialized:
            logger.info(f"{self.name} updating psyche...")
        self.psyche.update_state(utterance=utterance, conflict=conflict)

    def get_emotional_state(self):
        return self.psyche.get_emotional_state()

    def get_memory(self):
        return self.psyche.get_memory()

    def get_objective(self):
        return self.psyche.get_objective()

    def get_intention(self):
        return self.psyche.get_intention()

    def is_ending_conversation(self):
        return self.psyche.is_ending_conversation()
