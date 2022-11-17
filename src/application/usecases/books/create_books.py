from src.application.dtos.books_dto import BooksDTO
from src.application.interfaces.books_respository_interface import (
    BooksRepositoryInterface,
)
from src.domain.books.books_entity import BooksEntity


class CreateBooks:
    __repository: BooksRepositoryInterface

    def __init__(self, repository: BooksRepositoryInterface) -> None:
        self.__repository = repository

    def create(self, book: BooksDTO) -> None:
        new_book = BooksDTO.convert(BooksEntity(request=book))
        return self.__repository.create(book=new_book)
