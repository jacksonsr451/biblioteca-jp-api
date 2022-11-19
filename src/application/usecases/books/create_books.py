from src.application.dtos.books_dto import BooksDTO
from src.application.interfaces.books.create_books_interface import CreateBooksInterface
from src.application.interfaces.books_respository_interface import (
    BooksRepositoryInterface,
)
from src.domain.books.books_entity import BooksEntity
from src.domain.books.interfaces.books_dto_interface import BooksDTOInterface


class CreateBooks(CreateBooksInterface):
    __repository: BooksRepositoryInterface

    def __init__(self, repository: BooksRepositoryInterface) -> None:
        self.__repository = repository

    def create(self, book: BooksDTOInterface) -> None:
        new_book = BooksDTO.convert(BooksEntity(request=book))
        return self.__repository.create(book=new_book)
