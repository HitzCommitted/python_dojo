"""
Write a function that takes in a list of integers and returns True if it contains 007 in order
"""


def spy_game(nums):
    bond = ""
    for n in nums:
        if n == 0:
            bond += str(n)
        elif n == 7:
            bond += str(n)

    return bond == "007"


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))
