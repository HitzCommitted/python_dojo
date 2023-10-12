"""
Lambda Expressions Map and Filter
"""


def squares(num):
    return num**2


my_nums = [1, 3, 2, 4, 5, 6]

print(list(map(squares, my_nums)))


def splicer(my_string):
    if len(my_string) % 2 == 0:
        return "EVEN"
    else:
        return my_string[0]


names = ["Alex", "Diana", "Shiro", "Tomm", "Brad"]

print(list(map(splicer, names)))
