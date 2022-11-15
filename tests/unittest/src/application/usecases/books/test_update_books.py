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
    assert type(update_books.update(BooksDTO({}))) is NoneType
