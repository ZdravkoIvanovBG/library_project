from library import Library

def add_book_information():
    book_title = input("Title: ")
    author_name = input("Author: ")
    release_year = int(input("Release Year: "))

    return book_title, author_name, release_year

lib = Library()
lib.load_data()

while True:
    print("Available commands: add book, add reader, borrow book, return book, remove book, show books, show readers, sort books, finish")
    command = input("Command: ")

    if command.lower() == "finish":
        lib.save_data()
        print("Successfully saved data.")
        break

    try:
        if command.lower() == "add book":
            print("Book Types: E-Book, Book")
            type_of_book = input("Type of book: ")
            book_id = lib.generate_book_id()

            title, author, release_year = add_book_information()

            if type_of_book.lower() == "e-book":
                file_format = input("File format: ")
                file_size = int(input("File size: "))

                lib.add_e_book(file_format, file_size, book_id, title, author, release_year)
            elif type_of_book.lower() == "book":
                isbn = input("ISBN: ")
                pages = int(input("Pages: "))

                lib.add_book(isbn, pages, book_id, title, author, release_year)
            else:
                raise Exception("Invalid book type.")

            print("Successfully added book.")

        elif command.lower() == "add reader":
            reader_id = lib.generate_reader_id()
            name = input("Name: ")

            lib.add_reader(reader_id, name)

            print("Successfully added reader.")

        elif command.lower() == "borrow book":
            reader_name = input("Reader name: ")
            book_title = input("Book title: ")

            print(lib.borrow_book(reader_name, book_title))

        elif command.lower() == "return book":
            reader_name = input("Reader name: ")
            book_title = input("Book title: ")

            print(lib.return_book(reader_name, book_title))

        elif command.lower() == "remove book":
            book_title = input("Book title: ")

            print(lib.remove_book(book_title))

        elif command.lower() == "show books":
            lib.all_books()

        elif command.lower() == "show readers":
            lib.all_readers()

        elif command.lower() == "sort books":
            sort_by = input("Sort by: ")

            lib.sort_books(sort_by)

            print(f"Books sorted by {sort_by.capitalize()}.")

    except Exception as e:
        print(e)