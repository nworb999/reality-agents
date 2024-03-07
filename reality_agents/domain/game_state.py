from reality_agents.domain.conversation import ConversationManager

DEFAULT_ORDER_TYPE = "sequential"


class GameState:
    def __init__(self, characters, situation, max_turns):
        self.characters = characters
        self.situation = situation
        self.max_turns = max_turns
        self.conversations = []
        self.current_conversation = ConversationManager(
            characters=self.characters,
            situation=self.situation,
            order_type=DEFAULT_ORDER_TYPE,
        )
        self.current_character = 0
        self.current_turn = 0
        self.emotional_states = {character.name: "neutral" for character in characters}

    def start_new_conversation(self, situation=None, order_type=DEFAULT_ORDER_TYPE):
        if self.current_conversation:
            self.conversations.append(self.current_conversation)
        self.current_conversation = ConversationManager(
            characters=self.characters, situation=self.situation, order_type=order_type
        )
        for char in self.characters:
            char.initialize_state(
                situation if situation else self.situation, char.relationship_to_target
            )

        self.current_turn += 1

    def end_current_conversation(self):
        if self.current_conversation:
            self.conversations.append(self.current_conversation)
            self.current_conversation = None

    def continue_conversation(self, script):
        (
            current_turn,
            current_speaker,
            target,
            utterance,
        ) = self.current_conversation.next_line(script)
        self.current_turn = current_turn
        self.current_character = current_speaker
        return self.current_turn, self.current_character, target, utterance

    def update_emotional_state(self, character_name, new_state):
        if character_name in self.emotional_states:
            self.emotional_states[character_name] = new_state

    def is_game_over(self):
        return self.current_turn >= self.max_turns

    def get_emotional_state(self, character_name):
        return self.emotional_states.get(character_name, "unknown")
