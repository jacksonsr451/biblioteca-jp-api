from src.application.dtos.books_dto import BooksDTO
from src.application.interfaces.books_respository_interface import (
    BooksRepositoryInterface,
)


class CreateBooks:
    __repository: BooksRepositoryInterface

    def __init__(self, repository: BooksRepositoryInterface) -> None:
        self.__repository = repository

    def create(self, book: BooksDTO) -> None:
        return self.__repository.create(book=book)
