from reality_agents.domain.game_state import GameState

# includes creation of character logic, should not know details of conversation


# does it make sense to have
class GameLogic:
    def __init__(self, characters, conflict, scene, max_turns=10):
        self.characters = characters
        self.game_state = GameState(
            characters=characters, conflict=conflict, scene=scene, max_turns=max_turns
        )

    def reset_game(self):
        self.game_state.end_current_conversation()
        self.game_state.start_new_conversation()
        # initialize psyche for first character only
        # self.game_state.initialize_character_psyche(self.characters[0])

    def update_game(self, script):
        round_completed = False
        (
            current_turn,
            current_character,
            target,
            utterance,
        ) = self.game_state.continue_conversation(script)
        return current_turn, current_character, target, utterance, round_completed

    def is_game_over(self):
        return self.game_state.is_game_over()
