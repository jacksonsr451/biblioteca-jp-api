from datetime import date

import pytest

from src.domain.books.object_values.included_at_value import IncludedAtValue


@pytest.fixture(scope='class')
def included_at():
    return IncludedAtValue


def test_should_be_has_method(included_at) -> None:
    assert hasattr(included_at, 'value')


def test_should_be_return_types(included_at) -> None:
    assert type(included_at(date.today().strftime('d%-M%-Y%')).value()) is str


def test_should_be_return_new_value(included_at) -> None:
    assert included_at().value() is not None


def test_should_be_return_value(included_at) -> None:
    value: str = date.today().strftime('d%-M%-Y%')
    assert included_at(value).value().__eq__(value)
