from reality_agents.domain.conversation import ConversationManager
from utils.ascii import clear_screen, intro_text

DEFAULT_ORDER_TYPE = "sequential"


class GameState:
    def __init__(self, characters, conflict, scene, max_turns):
        self.characters = characters
        self.conflict = conflict
        self.scene = scene
        self.max_turns = max_turns
        self.conversations = []
        self.current_conversation = self._create_conversation()
        self.current_turn = 0

    def _create_conversation(
        self, conflict=None, scene=None, order_type=DEFAULT_ORDER_TYPE
    ):
        return ConversationManager(
            characters=self.characters,
            conflict=conflict or self.conflict,
            scene=scene or self.scene,
            order_type=order_type,
        )

    def _initialize_characters_psyche(self, conflict):
        for char in self.characters:
            char.initialize_psyche(conflict, char.relationship_to_target)

    def start_new_conversation(
        self, conflict=None, scene=None, order_type=DEFAULT_ORDER_TYPE
    ):
        clear_screen()
        intro_text()
        print("Generating conversation, this might take a while...")
        self._archive_current_conversation()
        self.current_conversation = self._create_conversation(
            conflict, scene, order_type
        )
        self._initialize_characters_psyche(conflict or self.conflict)
        self.current_turn += 1

    def _archive_current_conversation(self):
        if self.current_conversation:
            self.conversations.append(self.current_conversation)

    def end_current_conversation(self):
        self._archive_current_conversation()
        self.current_conversation = None

    def continue_conversation(self, script):
        (
            current_turn,
            current_speaker,
            target,
            utterance,
        ) = self.current_conversation.next_line(script)
        self.current_turn = current_turn
        return current_turn, current_speaker, target, utterance

    def is_game_over(self):
        if self.current_conversation and self.current_conversation.game_over:
            return "Game over: conversation ended"
        if self.current_turn >= self.max_turns:
            return "Game over: cutoff reached"
        return False
