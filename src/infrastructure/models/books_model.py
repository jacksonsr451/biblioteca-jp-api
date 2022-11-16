from sqlalchemy import Column, String

class BooksModelFactoring:
    __tablename__ = 'books'

    isbn = Column(String(36), primary_key=True)
    book_name = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    co_author = Column(String(255), nullable=True)
    publishing_company = Column(String(100), nullable=False)
    area = Column(String(50), nullable=False)
    shelf = Column(String(50), nullable=False)
    included_at = Column(String(9), nullable=True)
    updated_at = Column(String(9), nullable=True)

    def __repr__(self) -> str:
        return self.book_name.__str__()
