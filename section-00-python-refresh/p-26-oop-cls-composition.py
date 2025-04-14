# composition is inheritance counterpart to build classes that use other classes

class BookShelf:
    # *books will be a tuple of Book objects
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books\nBooks are: {', '.join(str(book) for book in self.books)}"
    
class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name!r}"

book = Book("Harry Potter")
book2 = Book("Lord of the Rings")
shelf = BookShelf(book, book2)

print(shelf)
print(f"{(', '.join(str(book) for book in shelf.books))}")
