#!/usr/bin/python3
"""
Defines a text-indentation function.
Module test_indentation
Prints a text with 2 new lines after each of these character.
"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # c = 0
    # while c < len(text) and text[c] == ' ':
    #     c += 1

    # while c < len(text):
    #     print(text[c], end="")
    #     if text[c] == "\n" or text[c] in ".?:":
    #         if text[c] in ".?:":
    #             print("\n")
    #         c += 1
    #         while c < len(text) and text[c] == ' ':
    #             c += 1
    #         continue
    #     c += 1

# THE BELOW ALGORITHM WORKS TOO, BUT 2 CASES FAILED IN THE TEXT CASE
# for delim in ".:?":
# text = (delim + "\n\n").join([line.strip(" ") for line in text.split(delim)])
# print(f"{text}", end="")
