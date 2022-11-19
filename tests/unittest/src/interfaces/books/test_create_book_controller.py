from types import NoneType
import pytest
from src.application.dtos.books_dto import BooksDTO
from src.application.interfaces.book_request_interface import BookRequestInterface
from src.application.interfaces.books_respository_interface import BooksRepositoryInterface

from src.interfaces.books.create_book_controller import CreateBookController
from src.application.usecases.books.create_books import CreateBooks


@pytest.fixture
def book_request():
    class RequestBooks(BookRequestInterface):
        pass
    return RequestBooks()


@pytest.fixture
def test_create_book_controller():  
    return CreateBookController

@pytest.fixture
def usecase_create_book():
    class BookRepository(BooksRepositoryInterface):
        def show(self) -> list[BooksDTO]:
            return super().show()
        
        def view(self, isbn: str) -> BooksDTO:
            return super().view(isbn)

        def create(self, book: BooksDTO) -> None:
            return super().create(book)

        def update(self, book: BooksDTO) -> None:
            return super().update(book)

        def delete(self, isbn: str) -> None:
            return super().delete(isbn)
            
    return CreateBooks(repository=BookRepository())

@pytest.fixture
def create_book_controller(usecase_create_book):
    return CreateBookController(controller=usecase_create_book)


def test_should_be_has_methods(create_book_controller) -> None:
    assert getattr(create_book_controller, 'execute')

def test_should_be_return_type(create_book_controller, book_request) -> None:
    assert type(create_book_controller.execute(request=book_request)) is NoneType
