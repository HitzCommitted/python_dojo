"""
Write a Python function that checks whether a word or phrase is palindrome or not.
"""


def palindrome(my_string):
    combined_str = my_string.replace(" ", "").lower()
    reverse_str = combined_str[::-1]

    return combined_str == reverse_str


print(palindrome("Kayak"))
