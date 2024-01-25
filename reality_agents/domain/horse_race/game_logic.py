class HorseRaceLogic:
    def __init__(self):
        self.progress1 = 0
        self.progress2 = 0
        self.target = 100

    def reset_game(self):
        self.progress1 = 0
        self.progress2 = 0

    def roll(self):
        import random

        return random.randint(10, 20)

    def play_round(self):
        self.update_progress(1)
        # should i check for a winner immediately after a roll?
        self.update_progress(2)
        return None

    def update_progress(self, player_number):
        roll_value = self.roll()
        if player_number == 1:
            self.progress1 = min(self.progress1 + roll_value, self.target)
        else:
            self.progress2 = min(self.progress2 + roll_value, self.target)

        self.check_winner()

    def check_winner(self):
        if self.progress1 >= self.target:
            return 1
        elif self.progress2 >= self.target:
            return 2
        return None
