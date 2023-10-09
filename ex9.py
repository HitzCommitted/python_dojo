def myFunc(*args):
    return sum((args))


print(myFunc(1, 100, 101))


def myFunc(**kwargs):
    if "name" in kwargs:
        print(f"My name is {kwargs['name']}")
    else:
        print("I did not find any name")


myFunc(name="alex", age=32)
myFunc(name="dee", age=33)
myFunc(name="soi", age=28)
myFunc(age=76)


def myFunc(*args, **kwargs):
    print(
        f"I would like {args[0]} students to eat {kwargs['meal']} with {kwargs['fruit']} every {kwargs['day']} at {kwargs['time']}"
    )


myFunc(10, 15, 49, 18, fruit="apples", meal="pizza", day="monday", time="noon")
