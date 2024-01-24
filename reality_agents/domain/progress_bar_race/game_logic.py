class ProgressBarRaceLogic:
    def __init__(self):
        self.progress1 = 0
        self.progress2 = 0
        self.target = 100

    def reset_game(self):
        # Reset the progress of both players to 0
        self.progress1 = 0
        self.progress2 = 0

    def roll(self):
        import random
        return random.randint(1, 10)

    def update_progress(self, player_number):
        roll_value = self.roll()
        if player_number == 1:
            self.progress1 = min(self.progress1 + roll_value, self.target)
        else:
             self.progress2 = min(self.progress2 + roll_value, self.target)  # Cap at 100

        self.check_winner()

    def check_winner(self):
        if self.progress1 >= self.target:
            return 1
        elif self.progress2 >= self.target:
            return 2
        return None
