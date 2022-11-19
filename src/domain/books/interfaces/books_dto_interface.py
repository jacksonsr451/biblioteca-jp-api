from abc import ABC, abstractmethod
from typing import Any


class BooksDTOInterface(ABC):
    isbn: str
    book_name: str
    author: str
    co_author: list
    publishing_company: str
    area: str
    shelf: str
    included_at: str
    updated_at: str

    @classmethod
    @abstractmethod
    def convert(cls, entity) -> Any:
        '''This method is required!'''

    @abstractmethod
    def to_dict(self) -> dict:
        '''This method is required!'''
