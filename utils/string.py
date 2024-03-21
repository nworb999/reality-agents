import re
import ast
import re

THEN_PRESS_ENTER = " (then press enter) "


def parse_utterance(input_string, remove_strings):
    # Remove all occurrences of '\n'
    cleaned_string = input_string.replace("\n", "").replace("[", "(").replace("]", ")")

    # Remove anything within parentheses (including the parentheses)
    cleaned_string = re.sub(r"\(.*?\)", "", cleaned_string)

    for remove_string in remove_strings:
        # Remove text that is in all caps and matches any string in the array
        if remove_string.upper() in cleaned_string:
            cleaned_string = cleaned_string.replace(remove_string.upper(), "")

        # Check and remove the string in all caps followed by ':'
        if remove_string + ":" in cleaned_string:
            cleaned_string = cleaned_string.replace(remove_string + ":", "")

    # Remove any '"' that directly follow ')'
    cleaned_string = cleaned_string.replace(')"', ")").replace(') "', ") ")

    return cleaned_string.strip().strip('"')


def parse_emotion_response(input_string):
    match = re.search(r"\{(.*?)\}", input_string, re.DOTALL)

    if match:
        # Extract the dictionary string and convert it to a dictionary using ast.literal_eval
        dict_string = match.group(0)

        # Remove comments starting with // or #
        dict_string = re.sub(r"(?://|#).*", "", dict_string)

        return ast.literal_eval(dict_string)
    else:
        return None


def check_yes_or_no(input_string):
    input_string = input_string.lower().strip()
    if "yes" in input_string:
        return True
    elif "no" or "not" in input_string:
        return False
    else:
        return None


# objective as less dynamic, intention as next-line specific


def starts_with_yes(sentence):
    sentence = sentence.strip().lower()
    if sentence.startswith("yes"):
        return "Yes"
    elif sentence.startswith("no"):
        return "No"
    else:
        return "The sentence does not start with Yes or No."
