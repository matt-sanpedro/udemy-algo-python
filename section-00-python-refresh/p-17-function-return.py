def add(x, y):
    return x + y

result = add(6, 4)
# by default, functions return None
print(result)

def subtract(x, y):
    print(x - y)
print(subtract(6, 4)) # OUTPUT: 2, None

# will NOT reach print statement in multiply function
def multiply(x, y):
    return x * y
    print(x * y)

result = multiply(6, 4) 
print(result)

# return will terminate the function and return the value to the caller
# NOT a good practice to have multiple return statements with different data types
def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You cannot divide by zero"

result = divide(1,0)
print(result)
result = divide(15,5)
print(result)
