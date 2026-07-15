from datetime import datetime
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, book_id: int, title: str, author: str, release_year: int, availability: bool):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.release_year = release_year
        self._availability = availability

    @property
    def release_year(self):
        return self.__release_year

    @release_year.setter
    def release_year(self, value):
        if value < 1 or value > datetime.now().year:
            raise ValueError("Invalid release year")
        self.__release_year = value

    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

    def is_available(self):
        return self._availability

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Release Year: {self.release_year}, Availability: {self._availability}"