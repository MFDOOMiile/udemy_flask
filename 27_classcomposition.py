###~~~Class Composition~~~###
class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book = Book("My Neighbor Totoro")
book2 = Book("Howl's Moving Castle")
book3 = Book("Porco Rosso")
shelf = BookShelf(book, book2, book3)

print(shelf)