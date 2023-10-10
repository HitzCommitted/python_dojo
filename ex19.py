"""
Return the sum of the numbers in the array, except ignore sections of numbers starting 
with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). 
Return 0 for no numbers
"""


def summer_69(arr):
    total = 0
    if 6 in arr:
        del arr[arr.index(6) : arr.index(9) + 1]
        total = sum(arr)
    else:
        total = sum(arr)
    return total


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
