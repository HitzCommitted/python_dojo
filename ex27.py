"""
Write a Python function to multiply all the numbers in a list.
"""


def multiply(numbers):
    result = 1

    for num in numbers:
        result *= num

    return result


print(multiply([1, 2, 3, -4]))
