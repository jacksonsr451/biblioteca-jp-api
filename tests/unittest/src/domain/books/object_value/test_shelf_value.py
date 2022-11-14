import pytest

from src.domain.books.errors.shelf_error import ShelfError
from src.domain.books.object_values.shelf_value import ShelfValue


@pytest.fixture(scope='class')
def sheld():
    return ShelfValue


def test_should_be_has_methods(sheld) -> None:
    assert hasattr(sheld, 'value')


def test_should_be_return_types(sheld) -> None:
    assert type(sheld('12').value()) is str


def test_should_be_return_error(sheld) -> None:
    with pytest.raises(ShelfError) as context:
        sheld().value()
    assert context.value.message.__eq__('Plateleira é um campo obrigatório!')


def test_should_be_return_value(sheld) -> None:
    value: str = '12'
    assert sheld(value).value().__eq__(value)
