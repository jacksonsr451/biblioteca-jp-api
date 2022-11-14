from datetime import date

import pytest

from src.domain.books.object_values.updated_at_value import UpdatedAtValue


@pytest.fixture(scope='class')
def updated_at():
    return UpdatedAtValue


def test_should_be_has_method(updated_at) -> None:
    assert hasattr(updated_at, 'value')


def test_should_be_return_types(updated_at) -> None:
    assert type(updated_at(date.today().strftime('d%-M%-Y%')).value()) is str


def test_should_be_return_new_value(updated_at) -> None:
    assert updated_at().value() is not None


def test_should_be_return_value(updated_at) -> None:
    value: str = date.today().strftime('d%-M%-Y%')
    assert updated_at(value).value().__eq__(value)
