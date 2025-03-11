# x and y are parameters
def add(x, y):
    result = x + y
    print(result)

# 5 and 3 are arguments
add(5, 3)

def say_hello(name, surname):
    print(f"Hello, {name} {surname}!")

# Bob is a positional argument
say_hello("Bob", "Sagat")
say_hello(surname="Napolean", name="Dynamite")

def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You cannot divide by zero")

divide(1,0)
divide(15,5)

# in python, no spaces when passing arguments
divide(dividend=15, divisor=3)
