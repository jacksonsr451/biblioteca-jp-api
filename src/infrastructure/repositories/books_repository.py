from src.application.dtos.books_dto import BooksDTO
from src.application.interfaces.books_respository_interface import (
    BooksRepositoryInterface,
)
from src.infrastructure.models.books_model import BooksModel


class BooksRepository(BooksRepositoryInterface):
    __model: BooksModel

    def __init__(self) -> None:
        self.__model = BooksModel()

    def show(self) -> list[BooksDTO]:
        return super().show()

    def view(self, string: str) -> BooksDTO:
        return super().view(string)

    def create(self, book: BooksDTO) -> None:
        return super().create(book)

    def update(self, book: BooksDTO) -> None:
        return super().update(book)

    def delete(self, isbn: str) -> None:
        return super().delete(isbn)
