from reality_agents.domain.conversation.game_logic import (
    GameLogic,
)
from reality_agents.domain.conversation.character import Character
from reality_agents.domain.conversation.scene import Scene
from reality_agents.data.repository import create_memory_entry

# handles gameplay experience, like creating the characters and managing the script
# also
# how to manage speaking order in here


class ConversationService:
    def __init__(self, db, characters, scene):
        self.db = db
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

        utterance, current_character, round_completed = self.game.play_turn(self.script)

        turn_data = {
            "name": current_character["name"],
            "dialogue": utterance,
            "status": "ONGOING",
            "round_completed": round_completed,
        }

        self.script.append(turn_data)
        print(self.script)

        if round_completed:
            round_message = f"--- Round {self.game.current_round} completed ---"
            self.script.append(round_message)

        return turn_data

    # def store_data(self, current_turn, speaker):
    #     game_id = 'game 1'
    #     conversation_id = 'convo 1'
    #     round_id = 'round 1'
    #     create_memory_entry(self.db,game_id, conversation_id,round_id,current_turn,)
