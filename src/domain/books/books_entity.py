from src.domain.books.object_values.area_value import AreaValue
from src.domain.books.object_values.author_value import AuthorValue
from src.domain.books.object_values.book_name_value import BookNameValue
from src.domain.books.object_values.co_author_value import CoAuthorValue
from src.domain.books.object_values.isbn_value import ISBNValue
from src.domain.books.object_values.shelf_value import ShelfValue


class BooksEntity:
    __isbn: str
    __book_name: str
    __author: str
    __co_author: list
    __area: str
    __shelf: str
    __included_at: str
    __updated_at: str

    def __init__(self, request) -> None:
        self.__isbn = ISBNValue(isbn=request.get('isbn')).value()
        self.__book_name = BookNameValue(
            book_name=request.get('book_name')
        ).value()
        self.__author = AuthorValue(author=request.get('author')).value()
        self.__co_author = CoAuthorValue(
            co_author=request.get('co_author')
        ).value()
        self.__area = AreaValue(area=request.get('area')).value()
        self.__shelf = ShelfValue(shelf=request.get('shelf')).value()
        self.__included_at
        self.__updated_at

    def get_isbn(self) -> str:
        return self.__isbn

    def get_book_name(self) -> str:
        return self.__book_name

    def get_author(self) -> str:
        return self.__author

    def get_co_author(self) -> list:
        return self.__co_author

    def get_area(self) -> str:
        return self.__area

    def get_shelf(self) -> str:
        return self.__shelf

    def get_included_at(self) -> str:
        return self.__included_at

    def get_updated_at(self) -> str:
        return self.__updated_at
