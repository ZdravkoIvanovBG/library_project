class Reader:
    def __init__(self, reader_id, name):
        self.reader_id = reader_id
        self.name = name
        self.books = []

    def object_to_dict(self):
        return {
            "reader_id": self.reader_id,
            "name": self.name,
            "borrowed_books": [book.title for book in self.books]
        }

    @classmethod
    def from_dict_to_object(cls, data):
        return cls(data["reader_id"], data["name"])

    def __str__(self):
        return f"Reader: {self.name}, ID: {self.reader_id}"
        