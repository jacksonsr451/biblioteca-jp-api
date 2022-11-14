import pytest

from src.domain.books.errors.isbn_error import ISBNError


@pytest.fixture(scope='class')
def isbn_error():
    return ISBNError()


def test_should_be_has_attribute(isbn_error) -> None:
    assert getattr(isbn_error, 'message')


def test_should_be_message_has_equal(isbn_error) -> None:
    assert isbn_error.message.__eq__('ISBN não é valido!')
