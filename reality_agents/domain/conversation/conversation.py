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
            print(self.current_turn)
            self.current_turn = (self.current_turn + 1) % len(self.characters)
        return self.order[self.current_turn]

    def update_order_based_on_conversation(self, conversation_results):
        # Logic to update the order based on conversation results
        pass


class ConversationLogic:
    # track next character to speak in here
    # In the provided `GameLogic` class, the determination of whose turn it is to speak is primarily managed through the `self.current_turn` attribute. Here's how it works:
    #
    # 1. **Initialization**: When an instance of `GameLogic` is created, `self.current_turn` is implicitly assumed to start at `0` (though not explicitly set in `__init__`). This means the first character in the `self.characters` list is initially designated to speak first.
    #
    # 2. **Playing a Turn**: Each time the `play_turn` method is called, it performs the following actions:
    #   - **Increment Speaking Turn**: The method increments the speaking count for the character whose turn it is to speak (`self.speaking_turns[self.current_turn] += 1`), indicating that this character has spoken once more.
    #   - **Round Completion Check**: It checks if `self.current_turn` equals `self.num_characters - 1`, which means the last character in the list has just taken their turn. If so, the method increments `self.current_round` and sets `round_completed` to `True`, indicating a full round of turns has been completed.
    #   - **Turn Advancement**: `self.current_turn` is then updated to point to the next character in the list. This is done by incrementing `self.current_turn` and then using modulo division by `self.num_characters` to ensure the value cycles back to `0` once it exceeds the index of the last character. This means if `self.current_turn` was equal to `self.num_characters - 1` (the last character), after the update, it will cycle back to `0` (the first character), starting a new round of turns.
    #   - **Generating Utterance**: The method then gets the next line of dialogue (`utterance = self.conversation.next_line()`) to be spoken in the game's context. This call suggests that the actual content of the conversation or the decision of what to say might be managed by the `ConversationLogic` class.

    # 3. **Determining the Current Speaker**:
    #  - Right before the line `utterance = self.conversation.next_line()` is executed, `self.current_turn` holds the index of the character in `self.characters` whose turn it is to speak. This index can be used to identify the current speaker from the `self.characters` list.
    #
    # Therefore, the current speaker is determined by the index `self.current_turn` in the `self.characters` list at any given point in the game. Each call to `play_turn` advances this index, ensuring each character gets their turn in a cyclic order.

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
        if sum(self.speaking_turns) == 0:  # Check if it's the first round
            current_speaker_index = 0
        else:
            current_speaker_index = self.speaking_order_logic.next_speaker()

        self.speaking_turns[current_speaker_index] += 1

        current_speaker = self.characters[current_speaker_index]
        current_speaker_name = current_speaker["name"]

        convo_state = "start" if self.speaking_turns == 0 else "ongoing"
        prompt = format_prompt(
            convo_state=convo_state,
            personality=current_speaker["personality"],
            target=target["name"],
            target_personality=target["personality"],
        )

        get_response(prompt=prompt)

        utterance = f"{current_speaker_name} spoke"

        self.speaking_order_logic.update_order_based_on_conversation(
            self.speaking_turns
        )

        return utterance
