from books.book import Book
from library import Library
from unittest import TestCase

from reader import Reader


class TestLibrary(TestCase):
    def setUp(self):
        self.lib = Library()
        self.lib.books.append(Book("1234567890123", 120, 2, "The Hobbit", "Author", 1972))
        self.lib.add_e_book("PDF", 5, 6, "Harry Potter", "Author 2", 1990)
        self.lib.readers.append(Reader(1, "Zdravko Ivanov"))

    def test_set_invalid_year(self):
        with self.assertRaises(ValueError) as ex:
            self.lib.add_book("1234567890123", 250, 1, "Title", "Author", 2060)

        self.assertEqual("Invalid release year", str(ex.exception))

    def test_set_invalid_isbn(self):
        with self.assertRaises(Exception) as ex:
            self.lib.add_book("12345", 250, 1, "Title", "Author", 1950)

        self.assertEqual("Invalid ISBN.", str(ex.exception))

    def test_search_book(self):
        book = self.lib.search_book("The Hobbit")

        self.assertEqual("The Hobbit", book.title)

    def test_search_non_existent_book(self):
        with self.assertRaises(Exception) as ex:
            self.lib.search_book("Random Book")

        self.assertEqual("Book not found.", str(ex.exception))

    def test_search_valid_reader(self):
        reader = self.lib.search_reader("Zdravko Ivanov")

        self.assertEqual("Zdravko Ivanov", reader.name)

    def test_search_non_existent_reader(self):
        with self.assertRaises(Exception) as ex:
            self.lib.search_reader("Random Reader")

        self.assertEqual("Reader not found.", str(ex.exception))

    def test_add_book_with_valid_data(self):
        count = len(self.lib.books)

        message = self.lib.add_book("1234567890124", 100, 3, "Harry Potter", "Author 2", 1990)

        self.assertEqual(count + 1, len(self.lib.books))

        new_book = self.lib.books[-1]

        self.assertEqual("1234567890124", new_book.isbn)
        self.assertEqual("Harry Potter", new_book.title)
        self.assertEqual("Author 2", new_book.author)
        self.assertEqual(1990, new_book.release_year)
        self.assertEqual(100, new_book.pages)
        self.assertEqual(True, new_book.is_available())
        self.assertEqual(
            f"Book {new_book.title} with ISBN {new_book.isbn} added to the library.", message
        )

    def test_add_book_which_already_exists(self):
        count = len(self.lib.books)

        with self.assertRaises(Exception) as ex:
            self.lib.add_book("1234567890123", 120, 2, "Harry Potter", "Author 2", 1990)

        self.assertEqual("Book already exists.", str(ex.exception))
        self.assertEqual(count, len(self.lib.books))

    def test_add_e_book_with_valid_data(self):
        count = len(self.lib.books)

        message = self.lib.add_e_book("PDF", 5, 4, "Harry Potter", "Author 2", 1990)

        self.assertEqual(count + 1, len(self.lib.books))

        new_book = self.lib.books[-1]

        self.assertEqual("PDF", new_book.file_format)
        self.assertEqual(5, new_book.file_size)
        self.assertEqual("Harry Potter", new_book.title)
        self.assertEqual("Author 2", new_book.author)
        self.assertEqual(1990, new_book.release_year)
        self.assertEqual(True, new_book.is_available())
        self.assertEqual(
            f"Book {new_book.title} with File Format {new_book.file_format}/File Size: {new_book.file_size} added to the library as an e-book.", message
        )

    def test_add_e_book_which_already_exists(self):
        count = len(self.lib.books)

        with self.assertRaises(Exception) as ex:
            self.lib.add_e_book("PDF", 5, 6, "Harry Potter", "Author 2", 1990)

        self.assertEqual(count, len(self.lib.books))
        self.assertEqual("Book already exists.", str(ex.exception))

    def test_add_reader_with_valid_data(self):
        count = len(self.lib.readers)

        self.lib.add_reader(2, "John Doe")
        self.assertEqual(count + 1, len(self.lib.readers))

        new_reader = self.lib.readers[-1]

        self.assertEqual(2, new_reader.reader_id)
        self.assertEqual("John Doe", new_reader.name)

    def test_add_already_existent_reader(self):
        count = len(self.lib.readers)

        with self.assertRaises(Exception) as ex:
            self.lib.add_reader(1, "Zdravko Ivanov")

        self.assertEqual(count, len(self.lib.readers))
        self.assertEqual("Reader already exists.", str(ex.exception))
