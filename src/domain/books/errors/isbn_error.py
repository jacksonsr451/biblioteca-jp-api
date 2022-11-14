class ISBNError(Exception):
    message: str

    def __init__(self, message: str = 'ISBN não é valido!') -> None:
        self.message = message
        super().__init__(self.message)
