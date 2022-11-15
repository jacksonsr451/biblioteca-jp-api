from src.application.dtos.books_dto import BooksDTO
from src.application.interfaces.books_respository_interface import (
    BooksRepositoryInterface,
)


class UpdateBooks:
    __repository: BooksRepositoryInterface

    def __init__(self, repository: BooksRepositoryInterface) -> None:
        self.__repository = repository

    def update(self, book: BooksDTO) -> None:
        return self.__repository.update(book=book)
