from reality_agents.domain.conversation.conversation import ConversationLogic


# includes creation of character logic
class GameLogic:
    def __init__(self, characters, max_rounds=5):
        self.characters = characters
        self.conversation = ConversationLogic(characters=self.characters)
        self.num_characters = len(characters)
        self.speaking_turns = [0] * self.num_characters
        self.max_rounds = max_rounds
        # how to make this flexible for different speaking order?
        self.current_character = 0
        self.current_round = 0

    def reset_game(self):
        self.speaking_turns = [0] * len(self.characters)
        self.current_character = 0
        self.current_round = 0

    def play_turn(self):
        # increments speaking turn for that character
        self.speaking_turns[self.current_character] += 1
        round_completed = False

        # round completion check (fix this)
        if self.current_character == self.num_characters - 1:
            self.current_round += 1
            round_completed = True

        self.next_character = (self.current_character + 1) % self.num_characters

        utterance = self.conversation.next_line(self.characters[self.next_character])
        return utterance, self.next_character, round_completed

    def is_game_over(self):
        return self.current_round >= self.max_rounds
