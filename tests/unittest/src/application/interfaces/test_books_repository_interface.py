import pytest

from src.application.interfaces.books_respository_interface import (
    BooksRepositoryInterface,
)


@pytest.fixture(scope='class')
def books_repository_interface():
    return BooksRepositoryInterface


def test_should_be_has_methods(books_repository_interface):
    assert hasattr(books_repository_interface, 'show')
    assert hasattr(books_repository_interface, 'view')
    assert hasattr(books_repository_interface, 'create')
    assert hasattr(books_repository_interface, 'update')
    assert hasattr(books_repository_interface, 'delete')
