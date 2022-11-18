import pytest

from src.infrastructure.models.books_model import BooksModel


@pytest.fixture(scope='class')
def books_model():
    return BooksModel()


def test_should_be_has_attributes(books_model) -> None:
    assert hasattr(books_model, 'isbn')
    assert hasattr(books_model, 'book_name')
    assert hasattr(books_model, 'author')
    assert hasattr(books_model, 'co_author')
    assert hasattr(books_model, 'publishing_company')
    assert hasattr(books_model, 'area')
    assert hasattr(books_model, 'shelf')
    assert hasattr(books_model, 'included_at')
    assert hasattr(books_model, 'updated_at')


def test_should_be_has_methods(books_model) -> None:
    assert getattr(books_model, '__repr__')


def test_should_be_return_types(books_model) -> None:
    assert type(books_model.__repr__()) is str


def test_should_be_return_values(books_model) -> None:
    assert books_model.__repr__().__eq__(
        '<BooksModel(isbn=None, book_name=None, author=None, co_author=None, publishing_company=None, area=None, shelf=None, included_at=None, updated_at=None)>'
    )
