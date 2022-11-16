import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection

load_dotenv()


class Model:
    engine = create_engine(
        'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
            os.getenv('DB_USERNAME'),
            os.getenv('DB_PASSWORD'),
            os.getenv('DB_HOST'),
            os.getenv('DB_PORT'),
            os.getenv('DB_NAME'),
        )
    )
    connection: Connection

    def connect(self):
        self.connection = self.engine.connect()

    def close(self):
        self.connection.close()
