from reality_agents.domain.conversation import ConversationManager


# includes creation of character logic
class GameLogic:
    def __init__(self, characters, max_rounds=5):
        self.characters = characters
        self.conversation = ConversationManager(characters=self.characters)
        self.max_rounds = max_rounds
        # how to make this flexible for different speaking order?
        self.current_character = 0
        self.current_round = 0

    def reset_game(self):
        self.current_character = 0
        self.current_round = 0

    def play_turn(self, script):
        round_completed = False

        current_turn, current_speaker, target, utterance = self.conversation.next_line(
            script
        )
        self.current_character = current_speaker

        # this will not always be the case
        # if self.current_character == len(self.characters) - 1:
        #     self.current_round += 1
        #     round_completed = True

        return current_turn, self.current_character, target, utterance, round_completed

    def is_game_over(self):
        return self.current_round >= self.max_rounds
