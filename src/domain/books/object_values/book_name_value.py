from src.domain.books.errors.book_name_error import BookNameError


class BookNameValue:
    __book_name: str

    def __init__(self, book_name: str = '') -> None:
        self.__book_name = self.__validate(book_name=book_name)

    @classmethod
    def __validate(cls, book_name: str = '') -> str:
        if book_name:
            return book_name
        raise BookNameError

    def value(self) -> str:
        return self.__book_name
