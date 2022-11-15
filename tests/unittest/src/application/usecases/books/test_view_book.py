import pytest
from src.application.dtos.books_dto import BooksDTO
from src.application.usecases.books.view_books import ViewBooks

from tests.unittest.src.application.usecases.books.book_repository_mock import TestBookReposisotoryMock


@pytest.fixture(scope='class')
def view_books():
    return ViewBooks(repository=TestBookReposisotoryMock())


def test_should_be_has_methods(view_books) -> None:
    assert getattr(view_books, 'view')

def test_should_be_return_type(view_books) -> None:
    assert type(view_books.view('test')) is BooksDTO

