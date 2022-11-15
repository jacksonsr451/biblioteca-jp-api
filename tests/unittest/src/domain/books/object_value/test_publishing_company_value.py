import pytest
from src.domain.books.errors.publishing_company_error import PublishingCompanyError

from src.domain.books.object_values.publishing_company_value import PublishingCompanyValue


@pytest.fixture(scope='class')
def publishing_company():
    return PublishingCompanyValue


def test_should_be_has_methods(publishing_company) -> None:
    assert hasattr(publishing_company, 'value')

def test_should_be_return_type(publishing_company) -> None:
    assert type(publishing_company('Alta Books').value()) is str

def test_should_be_return_error(publishing_company) -> None:
    with pytest.raises(PublishingCompanyError) as context:
        publishing_company().value()
    assert context.value.message.__eq__('Editora é um campo obrigatório!')

def test_should_be_return_value(publishing_company) -> None:
    value: str = 'Alta Books'
    assert publishing_company(value).value().__eq__(value)
