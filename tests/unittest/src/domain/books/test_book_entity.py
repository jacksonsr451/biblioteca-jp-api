from datetime import date

import pytest

from src.domain.books.books_entity import BooksEntity


@pytest.fixture
def books_request():
    class TestBooksRequest:
        isbn: str = '978-85-508-0460-6'
        book_name: str = 'Arquitetura Limpa'
        author: str = 'Robert C. Martin'
        co_author: list = []
        publishing_company: str = 'Alta Books'
        area: str = 'Listenning'
        shelf: str = '01'
        included_at: str = date.today().strftime('d%-M%-Y%')
        updated_at: str = date.today().strftime('d%-M%-Y%')

    return TestBooksRequest()


@pytest.fixture
def books_entity(books_request):
    return BooksEntity(request=books_request)


def test_should_be_has_methods(books_entity) -> None:
    assert hasattr(books_entity, 'get_isbn')
    assert hasattr(books_entity, 'get_book_name')
    assert hasattr(books_entity, 'get_author')
    assert hasattr(books_entity, 'get_co_author')
    assert hasattr(books_entity, 'get_publishing_company')
    assert hasattr(books_entity, 'get_area')
    assert hasattr(books_entity, 'get_shelf')
    assert hasattr(books_entity, 'get_included_at')
    assert hasattr(books_entity, 'get_updated_at')


def test_should_be_return_types(books_entity) -> None:
    assert type(books_entity.get_isbn()) is str
    assert type(books_entity.get_book_name()) is str
    assert type(books_entity.get_author()) is str
    assert type(books_entity.get_co_author()) is list
    assert type(books_entity.get_publishing_company()) is str
    assert type(books_entity.get_area()) is str
    assert type(books_entity.get_shelf()) is str
    assert type(books_entity.get_included_at()) is str
    assert type(books_entity.get_updated_at()) is str


def test_should_be_return_values(books_entity, books_request) -> None:
    assert books_entity.get_isbn().__eq__(books_request.isbn)
    assert books_entity.get_book_name().__eq__(books_request.book_name)
    assert books_entity.get_author().__eq__(books_request.author)
    assert books_entity.get_co_author().__eq__(books_request.co_author)
    assert books_entity.get_publishing_company().__eq__(
        books_request.publishing_company
    )
    assert books_entity.get_area().__eq__(books_request.area)
    assert books_entity.get_shelf().__eq__(books_request.shelf)
    assert books_entity.get_included_at().__eq__(books_request.included_at)
    assert books_entity.get_updated_at().__eq__(books_request.updated_at)
