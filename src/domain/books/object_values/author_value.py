from src.domain.books.errors.author_error import AuthorError


class AuthorValue:
    __author: str

    def __init__(self, author: str = '') -> None:
        self.__author = self.__validate(author=author)

    @classmethod
    def __validate(cls, author: str = '') -> str:
        if author:
            return author
        raise AuthorError

    def value(self) -> str:
        return self.__author
