from typing import Any
from src.domain.books.books_entity import BooksEntity


class BooksDTO:
    isbn: str
    book_name: str
    author: str
    co_author: list
    publishing_company: str
    area: str
    shelf: str
    included_at: str
    updated_at: str

    def __init__(self, request) -> None:
        self.isbn = request.get('isbn')
        self.book_name = request.get('book_name')
        self.author = request.get('author')
        self.co_author = request.get('co_author')
        self.publishing_company = request.get('publishing_company')
        self.area = request.get('area')
        self.shelf = request.get('shelf')
        self.included_at = request.get('included_at')
        self.updated_at = request.get('updated_at')

    @classmethod
    def convert(cls, entity: BooksEntity) -> Any:
        cls.isbn = entity.get_isbn()
        cls.book_name = entity.get_book_name()
        cls.author = entity.get_author()
        cls.co_author = entity.get_co_author()
        cls.publishing_company = entity.get_publishing_company()
        cls.area = entity.get_area()
        cls.shelf = entity.get_shelf()
        cls.included_at = entity.get_included_at()
        cls.updated_at = entity.get_updated_at()
        return cls

    def to_dict(self) -> dict:
        return {
            'isbn': self.isbn,
            'book_name': self.book_name,
            'author': self.author,
            'co_author': self.co_author,
            'publishing_company': self.publishing_company,
            'area': self.area,
            'shelf': self.shelf,
            'included_at': self.included_at,
            'updated_at': self.updated_at,
        }
