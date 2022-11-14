from email import message


class AreaError(Exception):
    message: str

    def __init__(self, message: str = 'Area é um campo obrigatório!') -> None:
        self.message = message
        super().__init__(message)
