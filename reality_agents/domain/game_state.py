from reality_agents.domain.conversation import ConversationManager

DEFAULT_ORDER_TYPE = "sequential"


class GameState:
    def __init__(self, characters, conflict, scene, max_turns):
        self.characters = characters
        self.conflict = conflict
        self.scene = scene
        self.max_turns = max_turns
        self.conversations = []
        self.current_conversation = ConversationManager(
            characters=self.characters,
            conflict=self.conflict,
            scene=self.scene,
            order_type=DEFAULT_ORDER_TYPE,
        )
        self.current_character = 0
        self.current_turn = 0

    def start_new_conversation(
        self, conflict=None, scene=None, order_type=DEFAULT_ORDER_TYPE
    ):
        if self.current_conversation:
            self.conversations.append(self.current_conversation)
        self.current_conversation = ConversationManager(
            characters=self.characters,
            conflict=conflict if conflict else self.conflict,
            scene=scene if scene else self.scene,
            order_type=order_type,
        )
        for char in self.characters:
            char.initialize_psyche(
                conflict if conflict else self.conflict, char.relationship_to_target
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

    def is_game_over(self):
        if self.current_conversation.game_over:
            return "Game over: conversation ended"
        if self.current_turn >= self.max_turns:
            return "Game over: cutoff reached"
        else:
            return False
