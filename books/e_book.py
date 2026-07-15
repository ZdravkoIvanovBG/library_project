from books.library_item import LibraryItem


class EBook(LibraryItem):
    def __init__(self, file_format, file_size, book_id, title, author, release_year, availability=True):
        super().__init__(book_id, title, author, release_year, availability)
        self.file_format = file_format
        self.file_size = file_size

    def borrow(self):
        # E-books have unlimited access, so availability never changes.
        self._availability = True

    def return_item(self):
        self._availability = True

    def object_to_dict(self):
        return {
            "book_type": "EBook",
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "release_year": self.release_year,
            "file_format": self.file_format,
            "file_size": self.file_size,
            "availability": self._availability
        }

    @classmethod
    def from_dict_to_object(cls, data):
        return cls(
            data["file_format"],
            data["file_size"],
            data["book_id"],
            data["title"],
            data["author"],
            data["release_year"],
            data["availability"]
        )

    def __str__(self):
        return f"E-Book: {self.title}, Author: {self.author}, Release Year: {self.release_year}, File Format: {self.file_format}, File Size: {self.file_size}"