# includes creation of character logic
class ConversationGameLogic:
    def __init__(self, characters, max_rounds=5):
        self.characters = characters
        self.num_characters = len(characters)
        self.speaking_turns = [0] * self.num_characters
        self.current_turn = 0
        self.max_rounds = max_rounds
        self.current_round = 0

    def reset_game(self):
        self.speaking_turns = [0] * len(self.characters)
        self.current_turn = 0
        self.current_round = 0

    def play_turn(self):
        self.speaking_turns[self.current_turn] += 1
        round_completed = False

        if self.current_turn == self.num_characters - 1:
            self.current_round += 1
            round_completed = True

        self.current_turn = (self.current_turn + 1) % self.num_characters
        return self.current_turn, round_completed

    def is_game_over(self):
        return self.current_round >= self.max_rounds
