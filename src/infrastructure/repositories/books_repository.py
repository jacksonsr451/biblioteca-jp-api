from src.application.dtos.books_dto import BooksDTO
from src.application.interfaces.books_respository_interface import (
    BooksRepositoryInterface,
)
from src.infrastructure.models.books_model import BooksModel
from src.infrastructure.services.connect import Connect


class BooksRepository(BooksRepositoryInterface):
    def __init__(self, connection: Connect) -> None:
        self.session = connection.connect()

    def show(self) -> list[BooksDTO]:
        list_books: list[BooksDTO] = list()
        for book in self.session.query(BooksModel).all():
            list_books.append(BooksDTO(book))
        return list_books

    def view(self, isbn: str) -> BooksDTO:
        book = self.session.query(BooksModel).filter_by(isbn=isbn)
        return BooksDTO(book)

    def create(self, book: BooksDTO) -> None:
        self.session.add(BooksModel(book=book))
        self.session.commit()

    def update(self, book: BooksDTO) -> None:
        update_book = (
            self.session.query(BooksModel)
            .filter(BooksModel.isbn == book.isbn)
            .first()
        )
        if update_book:
            update_book.author = book.author
            update_book.co_author = book.co_author
            update_book.book_name = book.book_name
            update_book.area = book.area
            update_book.shelf = book.shelf
            update_book.included_at = book.included_at
            update_book.updated_at = book.updated_at
            update_book.publishing_company = book.publishing_company
            self.session.commit()

    def delete(self, isbn: str) -> None:
        delete_book = (
            self.session.query(BooksModel).filter_by(isbn=isbn).first()
        )
        self.session.delete(delete_book)
        self.session.commit()
