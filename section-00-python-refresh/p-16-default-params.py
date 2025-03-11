def add(x, y=8):
    print(x + y)

add(5)
add(5, 8)

# cannot have default parameter followed by a non-default parameter
# below function throws error
# def subtract(x=3, y):
#     print(x - y)

# do not define variable outside of function
default_y = 3

def subtract(x, y=default_y):
    print(x - y)

subtract(2) # returns -1
default_y = 5
subtract(2) # returns -1, since default_y is defined before the function is called
