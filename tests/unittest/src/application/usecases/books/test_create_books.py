import warnings
from datetime import date
from types import NoneType

import pytest

from src.application.dtos.books_dto import BooksDTO
from src.application.usecases.books.create_books import CreateBooks
from src.domain.books.books_entity import BooksEntity
from tests.unittest.src.application.usecases.books.book_repository_mock import (
    TestBookReposisotoryMock,
)


@pytest.fixture(scope='class')
def create_books():
    return CreateBooks(repository=TestBookReposisotoryMock())


def test_should_be_has_methods(create_books) -> None:
    assert getattr(create_books, 'create')


def test_should_be_return_type(create_books) -> None:
    create_book = BooksDTO.convert(BooksEntity(request=TestBookRequest()))
    assert type(create_books.create(BooksDTO(request=create_book))) is NoneType


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
