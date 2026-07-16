import json

from books.book import Book
from books.e_book import EBook
from reader import Reader


class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    # Linear Time Complexity - O(n)
    def search_book(self, title):
        no_available_book = None

        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available():
                    return book # Return the first available book

                if no_available_book is None:
                    no_available_book = book # remember the first book of all unavailable ones

        if no_available_book:
            return no_available_book # if no available book exists, return the first unavailable book

        raise Exception("Book not found.")

    # Linear Time Complexity - O(n)
    def search_reader(self, name):
        for reader in self.readers:
            if reader.name.lower() == name.lower():
                return reader

        raise Exception("Reader not found.")

    def add_book(self, isbn, pages, book_id, title, author, release_year):
        for book in self.books:
            if book.book_id == book_id:
                raise Exception("Book already exists.")

        if not Book.isbn_validation(isbn):
            raise Exception("Invalid ISBN.")

        book = Book(isbn, pages, book_id, title, author, release_year)
        self.books.append(book)

        return f"Book {title} with ISBN {isbn} added to the library."

    def add_e_book(self, file_format, file_size, book_id, title, author, release_year):
        for book in self.books:
            if book.book_id == book_id:
                raise Exception("Book already exists.")

        e_book = EBook(file_format, file_size, book_id, title, author, release_year)
        self.books.append(e_book)

    def add_reader(self, reader_id, name):
        for reader in self.readers:
            if reader.reader_id == reader_id:
                raise Exception("Reader already exists.")

        reader = Reader(reader_id, name)
        self.readers.append(reader)

    def borrow_book(self, reader_name, book_title):
        reader = self.search_reader(reader_name)
        book = self.search_book(book_title)

        if len(reader.books) >= 3:
            raise Exception("Reader has too many books.")

        if book in reader.books:
            raise Exception("Book already borrowed by the reader.")

        if not book.is_available():
            raise Exception("Book is not available.")

        reader.books.append(book)
        book.borrow()

        return f"{reader.name} successfully borrowed {book.title}."

    def return_book(self, reader_name, book_title):
        reader = self.search_reader(reader_name)
        book = self.search_book(book_title)

        if book not in reader.books:
            raise Exception("Book not borrowed by the reader.")

        reader.books.remove(book)
        book.return_item()

        return f"{reader.name} successfully returned {book.title}."

    def remove_book(self, book_title):
        book = self.search_book(book_title)

        if not book.is_available():
            raise Exception("Book is not available and it can't be removed.")

        self.books.remove(book)
        return f"Book {book_title} removed from the library."

    def sort_books(self, sort_by):
        if sort_by == "title":
            self.books.sort(key=lambda book: book.title)
        elif sort_by == "year":
            self.books.sort(key=lambda book: book.release_year)
        else:
            raise ValueError("Invalid sort_by value. Use 'title' or 'year'.")


    def all_books(self):
        if not self.books:
            raise Exception("No books in the library.")

        for book in self.books:
            print(f"{book.title} - {book.author}/Release Year: {book.release_year}")

    def all_readers(self):
        if not self.readers:
            raise Exception("No readers in the library.")

        for reader in self.readers:
            print(f"Name: {reader.name} - {', '.join(book.title for book in reader.books) or "No"} books")

    def save_data(self):
        data = {
            "books": [book.object_to_dict() for book in self.books],
            "readers": [reader.object_to_dict() for reader in self.readers],
        }

        with open("library.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        try:
            with open("library.json", "r") as file:
                data = json.load(file)

            for book in data['books']:
                if book['book_type'] == 'Book':
                    self.books.append(Book.from_dict_to_object(book))
                else:
                    self.books.append(EBook.from_dict_to_object(book))

            for reader in data['readers']:
                reader_obj = Reader.from_dict_to_object(reader)

                self.readers.append(reader_obj)

                for book_title in reader['borrowed_books']:
                    book = self.search_book(book_title)
                    reader_obj.books.append(book)
                    book.borrow()

        except FileNotFoundError:
            self.books = []
            self.readers = []
            self.save_data()

    def generate_book_id(self):
        if not self.books:
            return 1

        return max(book.book_id for book in self.books) + 1

    def generate_reader_id(self):
        if not self.readers:
            return 1

        return max(reader.reader_id for reader in self.readers) + 1

    def __len__(self):
        return len(self.books)