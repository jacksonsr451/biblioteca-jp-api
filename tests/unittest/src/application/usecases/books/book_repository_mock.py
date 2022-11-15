import warnings
from src.application.dtos.books_dto import BooksDTO

from src.application.interfaces.books_respository_interface import BooksRepositoryInterface


class TestBookReposisotoryMock(BooksRepositoryInterface):
    def __init__(self) -> None:
        warnings.warn(UserWarning("Repositório de testes"))
        self.values: dict = {}

    def show(self) -> list[BooksDTO]:
        return [BooksDTO(request=self.values), BooksDTO(request=self.values)]
    
    def view(self, string: str) -> BooksDTO:
        return BooksDTO({})

    def create(self, book: BooksDTO) -> None:
        return super().create(book)
    
    def update(self, book: BooksDTO) -> None:
        return super().update(book)
    
    def delete(self, isbn: str) -> None:
        return super().delete(isbn)
