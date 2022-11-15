from src.application.dtos.books_dto import BooksDTO
from src.application.interfaces.books_respository_interface import (
    BooksRepositoryInterface,
)
from src.domain.books.books_entity import BooksEntity


class BooksUsecase:
    repository: BooksRepositoryInterface

    def __init__(self, repository: BooksRepositoryInterface) -> None:
        self.repository = repository

    def show(self) -> list[BooksDTO]:
        return self.repository.show()

    def view(self, string: str) -> BooksDTO:
        return self.view(string=string)

    def create(self, book: BooksDTO) -> None:
        self.repository.create(
            book=BooksDTO.convert(entity=BooksEntity(request=book.to_dict()))
        )

    def update(self, book: BooksDTO) -> None:
        self.repository.update(
            book=BooksDTO.convert(entity=BooksEntity(request=book.to_dict()))
        )

    def delete(self, isbn: str) -> None:
        self.repository.delete(isbn=isbn)
