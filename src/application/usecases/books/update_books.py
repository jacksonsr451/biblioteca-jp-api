from src.application.dtos.books_dto import BooksDTO
from src.application.interfaces.books_respository_interface import (
    BooksRepositoryInterface,
)
from src.domain.books.books_entity import BooksEntity


class UpdateBooks:
    __repository: BooksRepositoryInterface

    def __init__(self, repository: BooksRepositoryInterface) -> None:
        self.__repository = repository

    def update(self, book: BooksDTO) -> None:
        update_book = BooksDTO.convert(BooksEntity(request=book))
        return self.__repository.update(book=update_book)
