from datetime import date


class IncludedAtValue:
    __included_at: str

    def __init__(self, included_at: str = '') -> None:
        self.__included_at = self.__validate(included_at=included_at)

    @classmethod
    def __validate(cls, included_at) -> str:
        if included_at:
            return included_at
        return date.today().strftime('d%-M%-Y%')

    def value(self) -> str:
        return self.__included_at
