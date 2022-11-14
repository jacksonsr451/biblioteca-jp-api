import pytest

from src.domain.books.errors.shelf_error import ShelfError


@pytest.fixture(scope='class')
def shelf_error():
    return ShelfError()


def test_should_be_has_attribute(shelf_error) -> None:
    assert getattr(shelf_error, 'message')


def test_should_be_message_is_equal(shelf_error) -> None:
    assert shelf_error.message.__eq__('Plateleira é um campo obrigatório!')
