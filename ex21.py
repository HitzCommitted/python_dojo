"""
Lambda Expressions Map and Filter
"""


# Map function
def squares(num):
    return num**2


my_nums = [1, 3, 2, 4, 5, 6]

# print(list(map(squares, my_nums)))


def splicer(my_string):
    if len(my_string) % 2 == 0:
        return "EVEN"
    else:
        return my_string[0]


names = ["Alex", "Diana", "Shiro", "Tomm", "Brad"]

# print(list(map(splicer, names)))


# Filter function
def check_even(num):
    return num % 2 == 0


my_nums = [1, 2, 3, 4, 5, 6, 7, 8]

# print(list(filter(check_even, my_nums)))


# Lambda Expressions
# without lambda
def new_square(num):
    result = num**2
    return result


# with lambda
square = lambda num: num**2

# print(square(5))

print(list(map(lambda num: num**2, my_nums)))

print(list(filter(lambda num: num % 2 == 0, my_nums)))

print(list(map(lambda name: name[0], names)))
