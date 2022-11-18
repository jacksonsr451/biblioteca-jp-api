from sqlalchemy import Column, String

from src.domain.books.dtos.books_dto_interface import BooksDTOInterface
from src.infrastructure.models import Base


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

    def __init__(self, book: BooksDTOInterface | None = None) -> None:
        if book:
            self.isbn = book.isbn
            self.book_name = book.book_name
            self.author = book.author
            self.co_author = book.co_author
            self.publishing_company = book.publishing_company
            self.area = book.publishing_company
            self.shelf = book.shelf
            self.included_at = book.included_at
            self.updated_at = book.updated_at

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
