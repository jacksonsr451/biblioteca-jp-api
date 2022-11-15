from src.application.dtos.books_dto import BooksDTO
from src.application.interfaces.books_respository_interface import (
    BooksRepositoryInterface,
)


class ShowBooks:
    __repository: BooksRepositoryInterface

    def __init__(self, repository: BooksRepositoryInterface) -> None:
        self.__repository = repository

    def show(self) -> list[BooksDTO]:
        return self.__repository.show()
