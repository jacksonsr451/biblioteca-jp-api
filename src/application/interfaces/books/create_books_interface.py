from abc import ABC, abstractmethod

from src.domain.books.interfaces.books_dto_interface import BooksDTOInterface


class CreateBooksInterface(ABC):
    @abstractmethod
    def create(self, book: BooksDTOInterface) -> None:
        '''This methods is required!'''
