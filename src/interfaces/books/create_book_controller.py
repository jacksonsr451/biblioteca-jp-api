from src.application.dtos.books_dto import BooksDTO
from src.application.interfaces.book_request_interface import BookRequestInterface
from src.application.interfaces.books_respository_interface import BooksRepositoryInterface
from src.application.usecases.books.create_books import CreateBooks


class CreateBookController:
    
    def __init__(self, controller: CreateBooks, repository: BooksRepositoryInterface) -> None:
        self.controller = CreateBooks(repository=repository)

    def execute(self, request: BookRequestInterface) -> None:
        try:
            self.controller.create(book=BooksDTO(request=request))
        except Exception as error:
            print(error)
