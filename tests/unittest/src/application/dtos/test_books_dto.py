from datetime import date

import pytest

from src.application.dtos.books_dto import BooksDTO
from src.domain.books.books_entity import BooksEntity


@pytest.fixture
def request_books_dto():
    class TestBookRequest:
        isbn = '978-85-508-0460-6'
        book_name = 'book_name'
        author = 'author'
        co_author = ['']
        publishing_company = 'publishing_company'
        area = 'area'
        shelf = 'shelf'
        included_at = date.today().strftime('d%-M%-Y%')
        updated_at = date.today().strftime('d%-M%-Y%')

    return TestBookRequest


@pytest.fixture
def books_dto(request_books_dto):
    return BooksDTO(request=request_books_dto)


@pytest.fixture
def books_entity(request_books_dto):
    return BooksEntity(request={
        'isbn': '978-85-508-0460-6',
        'book_name': 'book_name',
        'author': 'author',
        'co_author': [''],
        'publishing_company': 'publishing_company',
        'area': 'area',
        'shelf': 'shelf',
        'included_at': date.today().strftime('d%-M%-Y%'),
        'updated_at': date.today().strftime('d%-M%-Y%'),
    })


def test_should_be_has_attributes(books_dto) -> None:
    assert getattr(books_dto, 'isbn')
    assert getattr(books_dto, 'book_name')
    assert getattr(books_dto, 'author')
    assert getattr(books_dto, 'co_author')
    assert getattr(books_dto, 'publishing_company')
    assert getattr(books_dto, 'area')
    assert getattr(books_dto, 'shelf')
    assert getattr(books_dto, 'included_at')
    assert getattr(books_dto, 'updated_at')


def test_should_be_return_types(books_dto) -> None:
    assert type(books_dto.isbn) is str
    assert type(books_dto.book_name) is str
    assert type(books_dto.author) is str
    assert type(books_dto.co_author) is list
    assert type(books_dto.publishing_company) is str
    assert type(books_dto.area) is str
    assert type(books_dto.shelf) is str
    assert type(books_dto.included_at) is str
    assert type(books_dto.updated_at) is str


def test_should_be_has_methods(books_dto) -> None:
    assert getattr(books_dto, 'convert')
    assert getattr(books_dto, 'to_dict')


def test_should_be_convert_and_compare_values(books_dto, books_entity) -> None:
    new_dto = BooksDTO.convert(entity=books_entity)

    assert new_dto.isbn.__eq__(books_dto.isbn)
    assert new_dto.book_name.__eq__(books_dto.book_name)
    assert new_dto.author.__eq__(books_dto.author)
    assert new_dto.co_author.__eq__(books_dto.co_author)
    assert new_dto.publishing_company.__eq__(books_dto.publishing_company)
    assert new_dto.area.__eq__(books_dto.area)
    assert new_dto.shelf.__eq__(books_dto.shelf)
    assert new_dto.included_at.__eq__(books_dto.included_at)
    assert new_dto.updated_at.__eq__(books_dto.updated_at)


def test_should_be_return_dict(books_dto) -> None:
    assert books_dto.to_dict().__eq__({
        'isbn': '978-85-508-0460-6',
        'book_name': 'book_name',
        'author': 'author',
        'co_author': [''],
        'publishing_company': 'publishing_company',
        'area': 'area',
        'shelf': 'shelf',
        'included_at': date.today().strftime('d%-M%-Y%'),
        'updated_at': date.today().strftime('d%-M%-Y%'),
    })
