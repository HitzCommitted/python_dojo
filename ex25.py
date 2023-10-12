"""
Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
"""


def up_low(my_string):
    upper = 0
    lower = 0

    for lett in my_string:
        if lett.isupper():
            upper += 1
        elif lett.islower():
            lower += 1

    count_string = f"No. of Upper case characters : {upper} \nNo. of Lower case characters : {lower}"

    return count_string


input_string = "Hello Mr. Rogers, how are you this fine Tuesday?"

print(up_low(input_string))
