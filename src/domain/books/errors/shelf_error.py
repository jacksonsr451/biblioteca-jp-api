from email import message


class ShelfError(Exception):
    message: str

    def __init__(
        self, message: str = 'Plateleira é um campo obrigatório!'
    ) -> None:
        self.message = message
        super().__init__(self.message)
