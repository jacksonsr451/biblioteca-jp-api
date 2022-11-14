from datetime import date


class UpdatedAtValue:
    __updated_at: str

    def __init__(self, updated_at: str = '') -> None:
        self.__include_at = self.__validate(updated_at=updated_at)

    @classmethod
    def __validate(cls, updated_at) -> str:
        if updated_at:
            return updated_at
        return date.today().strftime('d%-M%-Y%')

    def value(self) -> str:
        return self.__include_at
