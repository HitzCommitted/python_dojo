"""
Write a function that capitalizes the first and fourth letters of a name
"""


def old_macdonald(name):
    new_string = ""
    counter = 0

    for letter in name:
        if counter == 0 or counter == 3:
            new_string += letter.upper()
            counter += 1
        else:
            new_string += letter
            counter += 1

    return new_string


print(old_macdonald("macdonald"))
