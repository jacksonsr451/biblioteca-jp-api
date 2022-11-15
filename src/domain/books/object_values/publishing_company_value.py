from src.domain.books.errors.publishing_company_error import (
    PublishingCompanyError,
)


class PublishingCompanyValue:
    __publishing_company: str

    def __init__(self, publishing_company: str = '') -> None:
        self.__publishing_company = self.__validate(
            publishing_company=publishing_company
        )

    @classmethod
    def __validate(cls, publishing_company: str = '') -> str:
        if publishing_company:
            return publishing_company
        raise PublishingCompanyError

    def value(self) -> str:
        return self.__publishing_company
