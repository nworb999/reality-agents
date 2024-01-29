import random


class SpeakingOrderLogic:
    def __init__(self, characters, order_type="sequential"):
        self.characters = characters
        self.order_type = order_type
        self.current_turn = 0

        if order_type == "random":
            self.order = random.sample(range(len(characters)), len(characters))
        else:
            self.order = list(range(len(characters)))

    def next_speaker(self):
        if self.order_type == "random":
            self.current_turn = random.randint(0, len(self.characters) - 1)
        else:
            self.current_turn = (self.current_turn + 1) % len(self.characters)
        return self.order[self.current_turn]

    def update_order_based_on_conversation(self, conversation_results):
        # Logic to update the order based on conversation results
        pass


class ConversationLogic:
    def __init__(self, characters, order_type="sequential"):
        self.characters = characters
        self.speaking_turns = [0] * len(characters)
        self.speaking_order_logic = SpeakingOrderLogic(characters, order_type)

    def reset_game(self):
        self.speaking_turns = [0] * len(self.characters)
        self.speaking_order_logic = SpeakingOrderLogic(
            self.characters, self.speaking_order_logic.order_type
        )

    def play_turn(self):
        current_speaker_index = self.speaking_order_logic.next_speaker()
        self.speaking_turns[current_speaker_index] += 1
        current_speaker_name = self.characters[current_speaker_index].name

        announcement = f"{current_speaker_name} spoke"
        round_completed = self.speaking_order_logic.current_turn == 0

        # Update speaking order based on conversation results
        self.speaking_order_logic.update_order_based_on_conversation(
            self.speaking_turns
        )

        return announcement, round_completed
