from sqlalchemy.orm import declarative_base

from src.infrastructure.models.books_model import BooksModelFactoring

Base = declarative_base()

class BooksModel(Base, BooksModelFactoring):
    pass
