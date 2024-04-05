from reality_agents.domain.conversation import ConversationManager
from utils.ascii import clear_screen, intro_text
from utils.logger import logger

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

    def initialize_character_psyche(self, character, utterance=None):
        print(f"FOR {character.name}")
        character.initialize_psyche(
            conflict=self.conflict,
            scene=self.scene,
            relationship_to_target=character.relationship_to_target,
            utterance=utterance,
        )

    def update_character_psyche(self, character, utterance):
        character.update_psyche(
            conflict=self.conflict,
            utterance=utterance,
        )

    def start_new_conversation(
        self, conflict=None, scene=None, order_type=DEFAULT_ORDER_TYPE
    ):
        clear_screen()
        intro_text()
        logger.info("Generating conversation, this might take a while...")
        print("Generating conversation, this might take a while...")
        self._archive_current_conversation()
        self.current_conversation = self._create_conversation(
            conflict, scene, order_type
        )
        self.initialize_character_psyche(self.characters[0])

    def _archive_current_conversation(self):
        if self.current_conversation:
            self.conversations.append(self.current_conversation)

    def end_current_conversation(self):
        self._archive_current_conversation()
        self.current_conversation = None

    def continue_conversation(self, script):
        if self.current_turn == 1:
            # initialize psyche for second character using first thing said
            self.initialize_character_psyche(self.characters[1])
        (
            current_turn,
            current_speaker,
            target,
            utterance,
        ) = self.current_conversation.next_line(script)
        self.update_character_psyche(target, utterance)
        self.current_turn = current_turn
        return current_turn, current_speaker, target, utterance

    def is_game_over(self):
        if self.current_conversation and self.current_conversation.game_over:
            return "Game over: conversation ended"
        if self.current_turn >= self.max_turns:
            return "Game over: cutoff reached"
        return False
