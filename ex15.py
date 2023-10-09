"""
Given an integer n, return True if n is within 10 of either 100 or 200
"""


def almost_there(n):
    num = 10
    min_num = 100 - num
    max_num = 100 + num
    print(min_num, max_num)


almost_there(10)
