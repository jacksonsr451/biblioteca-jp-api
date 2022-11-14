import pytest

from src.domain.books.errors.isbn_error import ISBNError
from src.domain.books.object_values.isbn_value import ISBNValue


@pytest.fixture(scope='class')
def isbn_value():
    return ISBNValue


def test_should_be_has_method(isbn_value) -> None:
    assert hasattr(isbn_value, 'value')


def test_should_be_return_value(isbn_value) -> None:
    isbn: str = '978-85-508-0460-6'
    assert isbn_value(isbn).value().__eq__(isbn)


def test_should_be_return_error(isbn_value) -> None:
    isbn: str = '978-85-508-04600-6'
    with pytest.raises(ISBNError) as context:
        isbn_value(isbn).value()
    assert context.value.message.__eq__('ISBN não é valido!')

    isbn = '977-85-508-0460-6'
    with pytest.raises(ISBNError) as context:
        isbn_value(isbn).value()
    assert context.value.message.__eq__('ISBN não é valido!')

    isbn = '980-85-508-0460-6'
    with pytest.raises(ISBNError) as context:
        isbn_value(isbn).value()
    assert context.value.message.__eq__('ISBN não é valido!')
