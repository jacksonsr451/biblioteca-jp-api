from src.domain.books.errors.isbn_error import ISBNError


class ISBNValue:
    __isbn: str

    def __init__(self, isbn: str = '') -> None:
        self.__isbn = self.__validate(isbn=isbn)

    @classmethod
    def __validate(cls, isbn: str = '') -> str:
        value = isbn.split('-', 1)
        if not int(value[0]) in range(978, 979):
            raise ISBNError
        if not cls.__is_valid_isbn(isbn=''.join(value[1])):
            raise ISBNError
        return isbn

    @classmethod
    def __is_valid_isbn(cls, isbn: str = '') -> bool:
        code_string = isbn.replace('-', '').replace(' ', '')
        if len(code_string) != 10:
            return False
        if not code_string[0:8].isdigit() or not (
            code_string[9].isdigit() or code_string[9].lower() == 'x'
        ):
            return False

        result = 0

        for i in range(9):
            result = result + int(code_string[i]) * (10 - i)

        if code_string[9].lower() == 'x':
            result += 10
        else:
            result += int(code_string[9])

        if result % 11 == 0:
            return True
        else:
            return False

    def value(self) -> str:
        return self.__isbn
