import re


def is_list_def_string(string):
    """
    Determines if a string represents a list definition.

    Args:
        string (str): The string to be checked.

    Returns:
        tuple or None: If the string matches the pattern "{ANYTHING} = [{ANYTHING}]",
        returns a tuple containing the matched groups. Otherwise, returns None.
    """
    return re.match(r"(.*) = \[(.*)\]", string).groups()
    

def extract_list_from_def_list(string):
    """
    Extracts a list from a list definition string.

    Args:
        string (str): The list definition string.

    Returns:
        list or None: The extracted list if the input string is a valid list 
        definition string, otherwise None.
    """
    if is_list_def_string(string):
        return extract_string_between_brackets(string)
    return None

def extract_string_between_brackets(string):
    """
    Extracts the string between the first pair of brackets in the given string.

    Args:
        string (str): The input string from which to extract the string between brackets.

    Returns:
        str or None: The string between brackets if found, None otherwise.
    """
    return re.search(r"\[(.*?)\]", string).group(1) if re.search(r"\[(.*?)\]", string) else None
