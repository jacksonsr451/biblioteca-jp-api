from abc import ABC


class BookRequestInterface(ABC):
    isbn: str
    book_name: str
    author: str
    co_author: list
    publishing_company: str
    area: str
    shelf: str
    included_at: str
    updated_at: str
