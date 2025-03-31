def named(**kwargs):
    """
    This function accepts keyword arguments and prints them.
    The kwargs parameter collects all keyword arguments into a dictionary.
    """
    print(f"named data type: {type(kwargs)}")
    print(f"named arguments: {kwargs}")

named(name="Alice", age=30, city="New York")

def print_named(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}
print_named(**details)
named(**details)

def print_nicely(**kwargs):
    """
    This function prints keyword arguments in a nicely formatted way.
    """
    named(**kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_nicely(name="Charlie", age=35, city="Los Angeles")

def both(*args, **kwargs):
    """
    This function accepts both positional and keyword arguments.
    It prints the positional arguments and the keyword arguments separately.
    """
    print(f"both positional arguments: {args}")
    print(f"both keyword arguments: {kwargs}")

both(1, 2, 3, name="Dorothy", age=24)
