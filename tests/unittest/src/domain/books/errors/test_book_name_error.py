import pytest

from src.domain.books.errors.book_name_error import BookNameError


@pytest.fixture(scope='class')
def book_name():
    return BookNameError()


def test_should_be_has_attribute(book_name) -> None:
    assert getattr(book_name, 'message')


def test_should_be_message_is_equal(book_name) -> None:
    assert book_name.message.__eq__('Nome de livro é obrigatório!')
