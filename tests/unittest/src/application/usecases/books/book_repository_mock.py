import warnings
from datetime import date

from src.application.dtos.books_dto import BooksDTO
from src.application.interfaces.books_respository_interface import (
    BooksRepositoryInterface,
)


class TestBookRequest:
    def __init__(self) -> None:
        warnings.warn(UserWarning('Repositório de testes'))
        self.isbn = '978-85-508-0460-6'
        self.book_name = 'book_name'
        self.author = 'author'
        self.co_author = ['']
        self.publishing_company = 'publishing_company'
        self.area = 'area'
        self.shelf = 'shelf'
        self.included_at = date.today().strftime('d%-M%-Y%')
        self.updated_at = date.today().strftime('d%-M%-Y%')


class TestBookReposisotoryMock(BooksRepositoryInterface):
    def __init__(self) -> None:
        warnings.warn(UserWarning('Repositório de testes'))

    def show(self) -> list[BooksDTO]:
        return [
            BooksDTO(request=TestBookRequest()),
            BooksDTO(request=TestBookRequest()),
        ]

    def view(self, string: str) -> BooksDTO:
        return BooksDTO(request=TestBookRequest())

    def create(self, book: BooksDTO) -> None:
        return super().create(book)

    def update(self, book: BooksDTO) -> None:
        return super().update(book)

    def delete(self, isbn: str) -> None:
        return super().delete(isbn)
