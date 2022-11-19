from src.application.dtos.books_dto import BooksDTO
from src.application.interfaces.book_request_interface import BookRequestInterface
from src.application.interfaces.books.create_books_interface import CreateBooksInterface


class CreateBookController:
    
    def __init__(self, controller: CreateBooksInterface) -> None:
        self.controller = controller

    def execute(self, request: BookRequestInterface) -> None:
        try:
            self.controller.create(book=BooksDTO(request=request))
        except Exception as error:
            print(error)
