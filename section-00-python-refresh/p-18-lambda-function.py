# lambda function: does not have a name and is only used to return values
add = lambda x, y: x + y
print(add(2, 3))

# if a variable is not assigned to a lambda function, it will be garbage collected
# here is how to invoke a lambda function without assigning it to a variable
print((lambda x, y: x + y)(2, 3))

# revisiting the double function from p-16-function.py with list comprehension
def double(x):
    return x * 2

# list comprehension are more efficient than the map function
sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
print(doubled)

# can use map function on any sequence of lists, tuples, or sets
doubled = list(map(double, sequence))
print(doubled)

# better to use lambda function with map function, makes code clearer to read
doubled = list(map(lambda x: x * 2, sequence))
print(doubled)
