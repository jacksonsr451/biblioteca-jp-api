import pytest

from src.application.usecases.books.show_books import ShowBooks
from tests.unittest.src.application.usecases.books.book_repository_mock import (
    TestBookReposisotoryMock,
)


@pytest.fixture
def show_books():
    return ShowBooks(repository=TestBookReposisotoryMock())


def test_should_be_has_methods(show_books) -> None:
    assert getattr(show_books, 'show')


def test_should_be_return_type(show_books) -> None:
    assert type(show_books.show()) is list
