import pytest

from src.domain.books.errors.book_name_error import BookNameError
from src.domain.books.object_values.book_name_value import BookNameValue


@pytest.fixture(scope='class')
def book_name():
    return BookNameValue


def test_should_be_return_method(book_name) -> None:
    assert hasattr(book_name, 'value')


def test_should_be_return_type(book_name) -> None:
    assert type(book_name('Book Name').value()) is str


def test_should_be_return_error(book_name) -> None:
    with pytest.raises(BookNameError) as context:
        book_name().value()
    assert context.value.message.__eq__('Nome de livro é obrigatório!')
