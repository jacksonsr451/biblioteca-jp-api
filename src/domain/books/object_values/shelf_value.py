from src.domain.books.errors.shelf_error import ShelfError


class ShelfValue:
    __shelf: str

    def __init__(self, shelf: str = '') -> None:
        self.__shelf = self.__validate(shelf=shelf)

    @classmethod
    def __validate(cls, shelf: str = '') -> str:
        if shelf:
            return shelf
        raise ShelfError

    def value(self) -> str:
        return self.__shelf
