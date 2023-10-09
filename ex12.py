"""
Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. 
If not, return False
"""


def make_twenty(n1, n2):
    if sum((n1, n2)) == 20 or 20 in (n1, n2):
        return True
    else:
        return False


print(make_twenty(20, 10))
print(make_twenty(12, 8))
print(make_twenty(2, 3))
