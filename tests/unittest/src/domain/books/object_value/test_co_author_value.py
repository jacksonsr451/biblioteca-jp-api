import pytest

from src.domain.books.object_values.co_author_value import CoAuthorValue


@pytest.fixture(scope='class')
def co_author():
    return CoAuthorValue


def test_should_be_has_method(co_author) -> None:
    assert hasattr(co_author, 'value')


def test_should_be_return_types(co_author) -> None:
    assert type(co_author(['co author 1', 'co author 2']).value()) is list


def test_should_be_return_empty_list(co_author) -> None:
    assert co_author().value().__eq__(list())


def test_should_be_return_value(co_author) -> None:
    values: list = ['co author 1', 'co author 2']
    assert co_author(values).value().__eq__(values)
