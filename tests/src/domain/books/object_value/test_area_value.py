import pytest
from src.domain.books.errors.area_error import AreaError

from src.domain.books.object_values.area_value import AreaValue


@pytest.fixture(scope='class')
def area():
    return AreaValue

def test_should_be_has_methods(area) -> None:
    assert hasattr(area, 'value')

def test_should_be_return_types(area) -> None:
    assert type(area('A').value()) is str

def test_should_be_return_error(area) -> None:
    with pytest.raises(AreaError) as context:
        area().value()
    assert context.value.message.__eq__('Area é um campo obrigatório!')

def test_should_be_return_values(area) -> None:
    value: str = 'A'
    assert area(value).value().__eq__(value)
