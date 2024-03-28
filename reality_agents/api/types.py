from pydantic import BaseModel
from typing import List


class Character(BaseModel):
    name: str
    personality: str
    relationship_to_target: str


class GameRequest(BaseModel):
    characters: List[Character]
    conflict: str
    scene: str
    test_flag: bool
