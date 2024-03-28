import re
import re
import logging

THEN_PRESS_ENTER = " (then press enter) "


# Set up a logging handler to capture print statements
class PrintCaptureHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.latest_message = ""

    def emit(self, record):
        self.latest_message = self.format(record)


def parse_convo_summary(input_string):
    return input_string.strip()


def remove_artifacts(input_string: str):
    return input_string.replace(".,", ",").replace("..", ".")


def parse_init_intention(input_string):
    return input_string.strip().lower().replace("intention:", "")


def parse_initial_objective(input_string):
    lines = input_string.split("\n")
    result = {"objective": "", "tactics": []}

    in_objective = False
    in_tactics = False

    for line in lines:
        line = line.strip()

        if line.lower().startswith(("objective:", "* objective:")):
            in_objective = True
            in_tactics = False
            result["objective"] = line.split(":", 1)[-1].strip().replace(".", "")
            continue

        if line.startswith("Tactical Plan:"):
            in_objective = False
            in_tactics = True
            continue

        if not in_objective and (
            line.startswith("  - ") or line.split(". ", 1)[0].isdigit()
        ):
            tactic = line.split(". ", 1)[-1]
            result["tactics"].append(tactic)

    return result


def parse_utterance(input_string, remove_strings):
    # Remove all occurrences of '\n'
    cleaned_string = input_string.replace("\n", "").replace("[", "(").replace("]", ")")

    cleaned_string = re.sub(r"\(.*?\)", "", cleaned_string)

    for remove_string in remove_strings:
        if remove_string.upper() in cleaned_string:
            cleaned_string = cleaned_string.replace(remove_string.upper(), "")

        if remove_string + ":" in cleaned_string:
            cleaned_string = cleaned_string.replace(remove_string + ":", "")

    cleaned_string = cleaned_string.replace(')"', ")").replace(') "', ") ")

    return cleaned_string.strip().strip('"')


def parse_emotion_response(input_string):
    lines = input_string.split("\n")
    bullet_points = []

    for line in lines:
        clean_line = line.strip()
        if (
            clean_line.startswith("- ")
            or clean_line.startswith("* ")
            or clean_line.startswith("• ")
        ):
            bullet_point = clean_line.lstrip("-*• ").strip()
            # Check if there is a period in the bullet point
            if "." in bullet_point:
                # Extract the first sentence
                first_sentence = bullet_point.split(".")[0].strip()
                bullet_points.append(first_sentence)
            else:
                bullet_points.append(bullet_point)

    return "\n".join(bullet_points)


def check_yes_or_no(input_string):
    input_string = input_string.lower().strip()
    if "yes" in input_string:
        return True
    elif "no" or "not" in input_string:
        return False
    else:
        return None


def starts_with_yes(sentence):
    sentence = sentence.strip().lower()
    if sentence.startswith("yes"):
        return "Yes"
    elif sentence.startswith("no"):
        return "No"
    else:
        return "The sentence does not start with Yes or No."
