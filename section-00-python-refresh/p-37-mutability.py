a = []
b = a

# id function returns the location of the object in memory
print(id(a))
print(id(b))

a.append(25)
print(a)
print(b)
print(id(a))
print(id(b))

c = []
d = []
print(id(c))
print(id(d))

# a python list is mutable (or can be changed)
# a tuple in contract is immutable
