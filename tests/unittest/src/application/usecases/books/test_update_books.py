import warnings
from datetime import date
from types import NoneType

import pytest

from src.application.dtos.books_dto import BooksDTO
from src.application.usecases.books.update_books import UpdateBooks
from tests.unittest.src.application.usecases.books.book_repository_mock import (
    TestBookReposisotoryMock,
)


@pytest.fixture(scope='class')
def update_books():
    return UpdateBooks(repository=TestBookReposisotoryMock())


def test_should_be_has_methods(update_books) -> None:
    assert getattr(update_books, 'update')


def test_should_be_return_type(update_books) -> None:
    assert (
        type(update_books.update(BooksDTO(request=TestBookRequest())))
        is NoneType
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
