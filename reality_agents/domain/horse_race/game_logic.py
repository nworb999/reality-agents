import random


class HorseRaceLogic:
    def __init__(self, num_players=2):
        self.num_players = num_players
        self.progress = [0] * num_players
        self.current_turn = 0
        self.target = 100
        self.round_values = [0] * num_players

    def reset_game(self):
        self.progress = [0] * self.num_players
        self.current_turn = 0
        self.round_values = [0] * self.num_players

    def play_turn(self):
        roll = random.randint(10, 20)
        self.round_values[self.current_turn] = roll

        round_completed = False
        if self.current_turn == self.num_players - 1:
            self.update_progress()
            round_completed = True

        self.current_turn = (self.current_turn + 1) % self.num_players
        return None, round_completed

    def update_progress(self):
        for i in range(self.num_players):
            self.progress[i] = min(self.progress[i] + self.round_values[i], self.target)
        self.round_values = [0] * self.num_players

    def check_winner(self):
        for i, progress in enumerate(self.progress):
            if progress >= self.target:
                return i + 1
        return None
