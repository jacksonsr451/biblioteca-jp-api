import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

load_dotenv()


class Connect:
    DB_CONNECTION: str = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
        os.getenv('DB_USERNAME'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_HOST'),
        os.getenv('DB_PORT'),
        os.getenv('DB_NAME'),
    )

    @classmethod
    def __connect(cls):
        engine = create_engine(cls.DB_CONNECTION)
        connection = engine.connect()
        return connection

    @classmethod
    def session(cls):
        engine = create_engine(cls.DB_CONNECTION)
        Session = scoped_session(sessionmaker(sessionmaker(bind=engine)))
        session = Session(bind=cls.__connect())
        session.begin_nested()
        return session
