"""
Nested statements and scope
"""
# LOCAL
lambda num: num**2

# GLOBAL
name = "THIS IS A GLOBAL STRING"


def greet():
    # ENCLOSING
    name = "SAMMY"

    def hello():
        # LOCAL
        name = "I AM LOCAL"
        print("Hello " + name)

    hello()


# greet()


x = 50


def func():
    global x
    print(f"X is {x}")

    # LOCAL REASSIGNMENT
    x = "X GONNA GIVE IT TO YA!"
    print(f"I JUST LOCAL CHANGED X TO {x}")


func()
print(x)
