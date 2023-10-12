"""
Write a function that checks whether a number is in a given range (inclusive of high and low)
"""


def run_check(num, low, high):
    bool = num in [x for x in range(low, high + 1)]

    if bool:
        print(f"{num} IS IN the range between {low} and {high}")
    else:
        print(f"{num} IS NOT IN the range between {low} and {high}")
    return bool


print(run_check(10, 1, 10))
