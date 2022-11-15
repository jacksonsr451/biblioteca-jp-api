from src.application.dtos.books_dto import BooksDTO
from src.application.interfaces.books_respository_interface import (
    BooksRepositoryInterface,
)


class DeleteBooks:
    __repository: BooksRepositoryInterface

    def __init__(self, repository: BooksRepositoryInterface) -> None:
        self.__repository = repository

    def delete(self, isbn: str) -> None:
        return self.__repository.delete(isbn=isbn)
