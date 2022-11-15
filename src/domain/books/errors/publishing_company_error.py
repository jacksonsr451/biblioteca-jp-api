from email import message


class PublishingCompanyError(Exception):
    message: str

    def __init__(self, message: str = 'Editora é um campo obrigatório!') -> None:
        self.message = message
        super().__init__(self.message)