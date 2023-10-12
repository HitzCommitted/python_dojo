"""
Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
"""

import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    new_str = list(set(str1.replace(" ", "").lower()))
    new_str.sort()
    new_alphabet = "".join(new_str)

    return new_alphabet == alphabet


print(ispangram("The quick brown fox jumps over the lazy dog"))
