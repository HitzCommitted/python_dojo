"""
Given a sentence, return a sentence with the words reversed
"""


def master_yoda(text):
    split_text = text.split()
    split_text.reverse()
    reversed_string = " ".join(split_text)

    return reversed_string


print(master_yoda("I am home"))
print(master_yoda("We are ready"))
print(master_yoda("Programming is the key to success"))
