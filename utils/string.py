def strip_text(input_string, remove_strings):
    # Remove all occurrences of '\n'
    cleaned_string = input_string.replace("\n", "").replace("[", "(").replace("]", ")")

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
