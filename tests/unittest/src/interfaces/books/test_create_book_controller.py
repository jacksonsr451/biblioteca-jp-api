from types import NoneType
import pytest
from src.application.interfaces.book_request_interface import BookRequestInterface

from src.interfaces.books.create_book_controller import CreateBookController


@pytest.fixture
def book_request():
    class RequestBooks(BookRequestInterface):
        pass
    return RequestBooks()

@pytest.fixture
def create_book_controller():
    return CreateBookController(controller=None, repository=None)


def test_should_be_has_methods(create_book_controller) -> None:
    assert getattr(create_book_controller, 'execute')

def test_should_be_return_type(create_book_controller, book_request) -> None:
    assert type(create_book_controller.execute(request=book_request)) is NoneType
