import random
from typing import List, Dict, Tuple

from reality_agents.services.llm.prompt_injection import (
    format_did_conversation_end_prompt,
    format_intention_to_end_conversation_prompt,
    format_prompt,
)
from reality_agents.services.llm.ollama_handler import get_response
from utils.string import parse_utterance


def check_yes_or_no(input_string):
    input_string = input_string.lower().strip()
    if "yes" in input_string:
        return True
    elif "no" or "not" in input_string:
        return False
    else:
        return None


class SpeakingOrder:
    def __init__(self, num_characters: int, order_type: str = "sequential"):
        self.num_characters = num_characters
        self.order_type = order_type
        self.current_turn = -1
        self.order = self._initialize_order()

    def _initialize_order(self) -> List[int]:
        if self.order_type == "random":
            order = list(range(self.num_characters))
            random.shuffle(order)
            return order
        return list(range(self.num_characters))

    def next_speaker_index(self) -> int:
        if self.order_type == "random":
            self.current_turn = random.randint(0, self.num_characters - 1)
        else:
            self.current_turn = (self.current_turn + 1) % self.num_characters
        return self.order[self.current_turn]


class ConversationManager:
    def __init__(
        self,
        characters: List[Dict[str, str]],
        scene: str,
        conflict: str,
        order_type: str = "sequential",
    ):
        self.characters = characters
        self.conflict = conflict
        self.scene = scene
        self.turn = 0
        # (in order to track how active each character has been in the conversation)
        self.speaking_turns = [0] * len(characters)
        self.speaking_order = SpeakingOrder(len(characters), order_type)
        self.game_over = False

    def reset(self):
        self.turn = 0
        self.speaking_turns = [0] * len(self.characters)
        self.speaking_order = SpeakingOrder(
            len(self.characters), self.speaking_order.order_type
        )

    def _get_convo_state(self, current_speaker) -> str:
        if current_speaker.is_ending_conversation():
            return "ending"
        return "start" if sum(self.speaking_turns) == 0 else "ongoing"

    def _get_prompt(
        self,
        current_speaker: Dict[str, str],
        target: Dict[str, str],
        convo_state: str,
    ) -> str:
        return format_prompt(
            convo_state=convo_state,
            conflict=self.conflict,
            character=current_speaker,
            scene=self.scene,
            target=target,
        )

    def next_line(
        self, script: List[Dict[str, str]]
    ) -> Tuple[int, Dict[str, str], Dict[str, str], str]:
        current_speaker_index = self.speaking_order.next_speaker_index()
        current_speaker = self.characters[current_speaker_index]
        target = self.characters[(current_speaker_index + 1) % len(self.characters)]

        convo_state = self._get_convo_state(current_speaker=current_speaker)
        if convo_state == "ending":
            prompt = format_intention_to_end_conversation_prompt(
                current_speaker.personality,
                [entry["dialogue"] for entry in script] if script else None,
                current_speaker.get_objective(),
            )
            utterance = get_response(prompt, past_responses=None)
            # TODO is conversation over?
            over_prompt = format_did_conversation_end_prompt(
                utterances=None
                if self.turn == 0
                else [entry["dialogue"] for entry in script[:5]]
            )
            over_response = get_response(over_prompt)
            if check_yes_or_no(over_response):
                self.game_over = True
        else:
            prompt = self._get_prompt(current_speaker, target, convo_state)
            utterance = get_response(
                prompt=prompt,
                past_responses=None
                if self.turn == 0
                else [entry["dialogue"] for entry in script[:3]],
            )
        if self.turn != 0:
            target.update_psyche(
                conflict=self.conflict,
                convo_history=[entry["dialogue"] for entry in script[:3]],
            )

        self.speaking_turns[current_speaker_index] += 1
        self.turn += 1

        return self.turn, current_speaker, target, utterance
