class BookNameError(Exception):
    message: str

    def __init__(self, message: str = 'Nome de livro é obrigatório!') -> None:
        self.message = message
        super().__init__(self.message)
