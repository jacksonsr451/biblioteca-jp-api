import pytest

from src.domain.books.errors.author_error import AuthorError
from src.domain.books.object_values.author_value import AuthorValue


@pytest.fixture(scope='class')
def author():
    return AuthorValue


def test_should_be_return_method(author) -> None:
    assert hasattr(author, 'value')


def test_should_be_return_type(author) -> None:
    assert type(author('Author Name').value()) is str


def test_should_be_return_error(author) -> None:
    with pytest.raises(AuthorError) as context:
        author().value()
    assert context.value.message.__eq__('Autor é obrigátório!')
