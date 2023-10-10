"""
Given a string, return a string where for every character in the original there are three characters
"""


def paper_doll(text):
    return "".join([(x * 3) for x in text])


print(paper_doll("Mississippi"))
