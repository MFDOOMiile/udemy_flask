###~~~Type Hinting~~~###
from typing import List

def list_avg(sequence: list) -> float:  #the ": list" after sequence is the hint
    return sum(sequence) / len(sequence)

list_avg(123)


class Book:
    def __init__(self, name: str, page_count: int):  #": str & : int is the hint"
        self.name = name
        self.page_count = page_count

###~~~###
from typing import List         #can also import Tuple, Set, etc...

class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."


###~~~###

class Book:
    TYPES = ("hardcover", "paperback")  #example from class method, using hints

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book: {self.name}, it's a {self.book_type}, and it weighs {self.weight}g>"

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)