from src.application.dtos.books_dto import BooksDTO
from src.application.interfaces.books_respository_interface import (
    BooksRepositoryInterface,
)


class ViewBooks:
    __repository: BooksRepositoryInterface

    def __init__(self, repository: BooksRepositoryInterface) -> None:
        self.__repository = repository

    def view(self, string: str) -> BooksDTO:
        return self.__repository.view(string=string)
