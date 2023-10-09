"""
Write a function takes a two-word string and returns True if both words begin with same letter
"""


def animal_crackers(text):
    result = text.split()[0][0].lower() == text.split()[1][0].lower()
    return result


print(animal_crackers("Levelheaded Llama"))
print(animal_crackers("Crazy Kangaroo"))
print(animal_crackers("Sherlock Stones"))
