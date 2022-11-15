import pytest

from src.domain.books.errors.publishing_company_error import (
    PublishingCompanyError,
)


@pytest.fixture(scope='class')
def publishing_company_error():
    return PublishingCompanyError()


def test_should_be_has_attributes(publishing_company_error) -> None:
    assert getattr(publishing_company_error, 'message')


def test_should_be_message_is_equal(publishing_company_error) -> None:
    assert publishing_company_error.message.__eq__(
        'Editora é um campo obrigatório!'
    )
