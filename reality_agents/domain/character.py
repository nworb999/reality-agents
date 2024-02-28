from typing import Dict

# eventually Dict[str, str]
# in the future, mindstate and emotional state will be different


class Character:
    def __init__(self, name: str, personality: str):
        self.name: str = name
        self.personality: str = personality
        self.emotional_state: Dict[str, int]
