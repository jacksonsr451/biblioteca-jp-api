from lib2to3.pytree import Base

from sqlalchemy import Column, String

from src.infrastructure.services.sqlalchemy_service import Base


class BooksModel(Base):
    __tablename__ = 'books'

    isbn = Column(String(36), primary_key=True)
    book_name = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    co_author = Column(String(255), nullable=True)
    publishing_company = Column(String(100), nullable=False)
    area = Column(String(50), nullable=False)
    shelf = Column(String(50), nullable=False)
    included_at = Column(String(9), nullable=True)
    updated_at = Column(String(9), nullable=True)

    def __init__(self, book={}) -> None:
        self.isbn = book.get('isbn')
        self.book_name = book.get('book_name')
        self.author = book.get('author')
        self.co_author = book.get('co_author')
        self.publishing_company = book.get('publishing_company')
        self.area = book.get('area')
        self.shelf = book.get('shelf')
        self.included_at = book.get('included_at')
        self.updated_at = book.get('updated_at')

    def __repr__(self) -> str:
        return '<BooksModel(isbn={}, book_name={}, author={}, co_author={}, publishing_company={}, area={}, shelf={}, included_at={}, updated_at={})>'.format(
            self.isbn,
            self.book_name,
            self.author,
            self.co_author,
            self.publishing_company,
            self.area,
            self.shelf,
            self.included_at,
            self.updated_at,
        )
