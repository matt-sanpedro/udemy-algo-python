from operator import itemgetter

# first class function: function that behaves like a variable
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor

def calculate(*values, operator):
    print(f"Calculating with {operator.__name__} on {values}")
    print(f"Value is of type: {type(values)}")
    return operator(*values)

# exmaple use of first class function
result = calculate(20, 4, operator=divide)
print(result)

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 28},
    {"name": "Eve", "age": 22},
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Alice", get_friend_name))
print(search(friends, "Alice", lambda friend: friend["name"]))
print(search(friends, "Alice", itemgetter("name")))
