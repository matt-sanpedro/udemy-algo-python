class ClassTest:
    def instance_method(self):
        print(f"Called the instance_method of {self}")

    @classmethod
    # cls will be the class itself
    # used often as factories
    def class_method(cls):
        print(f"Called the class_method of {cls}")

    # does not have any access to the class or instance
    # places a method inside the class
    @staticmethod
    def static_method():
        print("Called the static_method")

# instantiate the class
test = ClassTest()

# two ways to call the instance_method
test.instance_method()
ClassTest.instance_method(test)

# calling the class method does not require an instance
ClassTest.class_method()

# factory example on how to use a class method
# in a class (like methods), can also place variables
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, {self.weight}g>"

    # book and cls are interchangeable
    # cls will come handy when using inheritance
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

# can access the tuple with print
print(Book.TYPES)

book = Book("The Hobbit", "hardcover", 1600+100)
print(book)

bookPotter = Book.hardcover("Harry Potter", 1800)
print(bookPotter)

bookLight = Book.paperback("Batman Comic", 100)
print(bookLight)
