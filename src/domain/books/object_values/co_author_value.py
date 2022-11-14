class CoAuthorValue:
    __co_author: list

    def __init__(self, co_author: list = []) -> None:
        self.__co_author = self.__validate(co_author=co_author)

    @classmethod
    def __validate(cls, co_author: list = []) -> list:
        if co_author:
            return co_author
        return list()

    def value(self) -> list:
        return self.__co_author
