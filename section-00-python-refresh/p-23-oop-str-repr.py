# magic methods: don't have to call it
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # method gets called when you turn the object into a string
    def __str__(self):
        return f"Person {self.name}, {self.age} years old."

    # method to return a string to recreate the object easily
    # also used by the Python debugger
    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"

bob = Person("Bob", 35)
print(bob) # python prints the memory address of the object

# call the repr method to see output
print(bob.__repr__())
