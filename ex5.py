"""
Write a program that prints the integers from 1 to 100. 
But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
For numbers which are both multiples of three and five print "FizzBuzz"
"""

for num in list(range(1, 101)):
    output = [int(x) for x in str(num)]
    sum_output = sum(output)

    if sum_output % 3 == 0:
        print("Fizz")
    elif sum_output % 5 == 0:
        print("Buzz")
    elif sum_output % 3 == 0 and sum_output % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)
