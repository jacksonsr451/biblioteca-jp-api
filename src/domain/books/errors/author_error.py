class AuthorError(Exception):
    message: str

    def __init__(self, message: str = 'Autor é obrigátório!') -> None:
        self.message = message
        super().__init__(self.message)
