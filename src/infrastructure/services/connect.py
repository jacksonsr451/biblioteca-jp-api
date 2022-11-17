import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()


class Connect:
    @classmethod
    def connect(cls):
        Session = sessionmaker(
            bind=create_engine(
                'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
                    os.getenv('DB_USERNAME'),
                    os.getenv('DB_PASSWORD'),
                    os.getenv('DB_HOST'),
                    os.getenv('DB_PORT'),
                    os.getenv('DB_NAME'),
                )
            )
        )
        return Session()
