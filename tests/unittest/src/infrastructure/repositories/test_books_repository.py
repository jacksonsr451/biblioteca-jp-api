from datetime import date
from types import NoneType

import pytest

from src.application.dtos.books_dto import BooksDTO
from src.application.interfaces.book_request_interface import BookRequestInterface
from src.infrastructure.repositories.books_repository import BooksRepository


@pytest.fixture
def books_repository(session):
    return BooksRepository(session=session)


@pytest.fixture
def books_dto():
    class TestBookRequest(BookRequestInterface):
        isbn = '978-85-508-0460-6'
        book_name = 'book_name'
        author = 'author'
        co_author = ['']
        publishing_company = 'publishing_company'
        area = 'area'
        shelf = 'shelf'
        included_at = date.today().strftime('d%-M%-Y%')
        updated_at = date.today().strftime('d%-M%-Y%')

    return BooksDTO(request=TestBookRequest())


def test_should_be_has_methods(books_repository) -> None:
    assert getattr(books_repository, 'show')
    assert getattr(books_repository, 'view')
    assert getattr(books_repository, 'create')
    assert getattr(books_repository, 'update')
    assert getattr(books_repository, 'delete')


def test_should_be_return_values(books_repository, books_dto) -> None:
    assert type(books_repository.show()) is list
    assert type(books_repository.create(book=books_dto)) is NoneType
    assert type(books_repository.view(isbn='978-85-508-0460-6')) is BooksDTO
    assert type(books_repository.update(book=books_dto)) is NoneType
    assert type(books_repository.delete(isbn='978-85-508-0460-6')) is NoneType
