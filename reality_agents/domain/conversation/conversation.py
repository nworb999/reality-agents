import random
from reality_agents.services.llm.prompt_injection import format_prompt
from reality_agents.services.llm.ollama_handler import get_response


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
        # in order to track how active each character has been in the conversation
        self.speaking_turns = [0] * len(characters)
        self.speaking_order_logic = SpeakingOrderLogic(characters, order_type)

    def reset_game(self):
        self.speaking_turns = [0] * len(self.characters)
        self.speaking_order_logic = SpeakingOrderLogic(
            self.characters, self.speaking_order_logic.order_type
        )

    def next_line(self, target=None):
        # check if it's the first round, otherwise default to next logic
        if sum(self.speaking_turns) == 0:
            current_speaker_index = 0
            convo_state = "start"
        else:
            current_speaker_index = self.speaking_order_logic.next_speaker()
            convo_state = "ongoing"

        self.speaking_turns[current_speaker_index] += 1

        current_speaker = self.characters[current_speaker_index]
        current_speaker_name = current_speaker["name"]

        prompt = format_prompt(
            convo_state=convo_state,
            character=current_speaker,
            target=target,
        )

        utterance = get_response(prompt=prompt)

        # utterance = f"{current_speaker_name} spoke"

        self.speaking_order_logic.update_order_based_on_conversation(
            self.speaking_turns
        )

        return utterance
