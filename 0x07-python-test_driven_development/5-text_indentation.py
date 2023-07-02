def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    result = ""
    line = ""

    for char in text:
        line += char

        if char in [".", "?", ":"]:
            result += line.strip() + "\n\n"
            line = ""

    result += line.strip()

    print(result)
