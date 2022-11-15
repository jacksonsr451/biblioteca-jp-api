from types import NoneType

import pytest

from src.application.dtos.books_dto import BooksDTO
from src.application.usecases.books.create_books import CreateBooks
from tests.unittest.src.application.usecases.books.book_repository_mock import (
    TestBookReposisotoryMock,
)


@pytest.fixture(scope='class')
def create_books():
    return CreateBooks(repository=TestBookReposisotoryMock())


def test_should_be_has_methods(create_books) -> None:
    assert getattr(create_books, 'create')


def test_should_be_return_type(create_books) -> None:
    assert type(create_books.create(BooksDTO({}))) is NoneType
