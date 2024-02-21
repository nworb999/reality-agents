from reality_agents.domain.conversation.conversation import ConversationLogic


# includes creation of character logic
class GameLogic:
    def __init__(self, characters, max_rounds=5):
        self.characters = characters
        self.conversation = ConversationLogic(characters=self.characters)
        self.max_rounds = max_rounds
        # how to make this flexible for different speaking order?
        self.current_character = 0
        self.current_round = 0

    def reset_game(self):
        self.current_character = 0
        self.current_round = 0

    def play_turn(self, script):
        round_completed = False

        utterance, current_speaker = self.conversation.next_line(script)
        self.current_character = current_speaker

        # this will not always be the case
        # if self.current_character == len(self.characters) - 1:
        #     self.current_round += 1
        #     round_completed = True

        return utterance, self.current_character, round_completed

    def is_game_over(self):
        return self.current_round >= self.max_rounds
