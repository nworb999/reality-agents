from reality_agents.domain.conversation.game_logic import (
    GameLogic,
)
from reality_agents.domain.conversation.character import Character
from reality_agents.domain.conversation.scene import Scene

# handles gameplay experience, like creating the characters and managing the script
# how to manage speaking order in here


class ConversationService:
    def __init__(self, characters, scene):
        self.game = GameLogic(characters)  # replace with gamestate?
        self.characters = [
            Character(character["name"], character["personality"])
            for character in characters
        ]
        self.scene = Scene(scene)
        self.script = []  # for later

    def start_game(self):
        self.game.reset_game()
        return f"New game started. {self.characters[0].name} goes first."

    def update(self):
        if self.game.is_game_over():
            return {"status": "FINISHED"}

        utterance, current_turn, round_completed = self.game.play_turn()
        turn_data = {
            "name": self.characters[current_turn].name,
            "dialogue": utterance,
            "status": "ONGOING",
            "round_completed": round_completed,
        }
        self.script.append(turn_data)
        if round_completed:
            round_message = f"--- Round {self.game.current_round} completed ---"
            self.script.append(round_message)

        return turn_data
