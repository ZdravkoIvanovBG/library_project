from books.library_item import LibraryItem


class Book(LibraryItem):
    def __init__(self, isbn, pages, book_id, title, author, release_year, availability=True):
        super().__init__(book_id, title, author, release_year, availability)
        self.isbn = isbn
        self.pages = pages

    def borrow(self):
        self._availability = False

    def return_item(self):
        self._availability = True

    def object_to_dict(self):
        return {
            "book_type": "Book",
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "release_year": self.release_year,
            "isbn": self.isbn,
            "pages": self.pages,
            "availability": self._availability
        }

    @classmethod
    def from_dict_to_object(cls, data):
        return cls(
            data["isbn"],
            data["pages"],
            data["book_id"],
            data["title"],
            data["author"],
            data["release_year"],
            data["availability"]
        )

    @staticmethod
    def isbn_validation(isbn):
        return isbn.isdigit() and len(isbn) == 13

    def __str__(self):
        return f"Book: {self.title}, Author: {self.author}, Release Year: {self.release_year}, ISBN: {self.isbn}, Pages: {self.pages}"