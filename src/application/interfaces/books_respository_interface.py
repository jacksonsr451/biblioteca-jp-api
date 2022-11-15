from abc import ABC, abstractmethod

from src.application.dtos.books_dto import BooksDTO


class BooksRepositoryInterface(ABC):
    @abstractmethod
    def show(self) -> list[BooksDTO]:
        """This method is required!"""

    @abstractmethod
    def view(self, string: str) -> BooksDTO:
        """This method is required!"""

    @abstractmethod
    def create(self, book: BooksDTO) -> None:
        """This method is required!"""

    @abstractmethod
    def update(self, book: BooksDTO) -> None:
        """This method is required!"""

    @abstractmethod
    def delete(self, isbn: str) -> None:
        """This method is required!"""
