"""
Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
"""
# nums_list = list(range(1, 50))

new_list = [num for num in list(range(1, 51)) if num % 3 == 0]

print(new_list)
