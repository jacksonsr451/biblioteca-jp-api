import pytest

from src.domain.books.errors.area_error import AreaError


@pytest.fixture(scope='class')
def area_error():
    return AreaError()


def test_should_be_has_attribute(area_error) -> None:
    assert getattr(area_error, 'message')


def test_should_be_message_has_equal(area_error) -> None:
    assert area_error.message.__eq__('Area é um campo obrigatório!')
