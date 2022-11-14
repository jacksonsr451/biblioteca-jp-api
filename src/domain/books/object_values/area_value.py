from src.domain.books.errors.area_error import AreaError


class AreaValue:
    __area: str

    def __init__(self, area: str = '') -> None:
        self.__area = self.__validate(area=area)

    @classmethod
    def __validate(cls, area: str = '') -> str:
        if area:
            return area
        raise AreaError

    def value(self) -> str:
        return self.__area
