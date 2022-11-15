from types import NoneType
import pytest
from src.application.usecases.books.delete_books import DeleteBooks

from tests.unittest.src.application.usecases.books.book_repository_mock import TestBookReposisotoryMock


@pytest.fixture(scope='class')
def delete_books():
    return DeleteBooks(repository=TestBookReposisotoryMock())


def test_should_be_has_methods(delete_books) -> None:
    assert getattr(delete_books, 'delete')

def test_should_be_return_type(delete_books) -> None:
    assert type(delete_books.delete('test')) is NoneType

