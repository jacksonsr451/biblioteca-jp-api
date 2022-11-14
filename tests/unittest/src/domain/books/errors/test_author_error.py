import pytest

from src.domain.books.errors.author_error import AuthorError


@pytest.fixture(scope='class')
def author_error():
    return AuthorError()


def test_should_be_has_attibute(author_error) -> None:
    assert getattr(author_error, 'message')


def test_should_be_message_has_equal(author_error) -> None:
    assert author_error.message.__eq__('Autor é obrigátório!')
