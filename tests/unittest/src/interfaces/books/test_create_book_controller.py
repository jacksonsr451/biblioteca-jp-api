from types import NoneType
import pytest
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
def book_repository():
    class BookRepository(BooksRepositoryInterface):
        pass 
    return BookRepository

@pytest.fixture
def usecase_create_book():
    return CreateBooks

@pytest.fixture
def create_book_controller(usecase_create_book, book_repository):
    return CreateBookController(controller=usecase_create_book, repository=book_repository)


def test_should_be_has_methods(create_book_controller) -> None:
    assert getattr(create_book_controller, 'execute')

def test_should_be_return_type(create_book_controller, book_request) -> None:
    assert type(create_book_controller.execute(request=book_request)) is NoneType
