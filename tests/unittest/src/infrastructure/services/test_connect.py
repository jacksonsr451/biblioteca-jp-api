import pytest
import os

from dotenv import load_dotenv

from src.infrastructure.services.connect import Connect

load_dotenv()

@pytest.fixture
def link_conection():
    return 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
        os.getenv('DB_USERNAME'),
        os.getenv('DB_PASSWORD'),
        os.getenv('DB_HOST'),
        os.getenv('DB_PORT'),
        os.getenv('DB_NAME'),
    )

@pytest.fixture
def class_connect():
    return Connect()


def test_should_be_has_methods(class_connect) -> None:
    assert getattr(class_connect, 'session')


def test_should_be_has_attributes(class_connect) -> None:
    assert hasattr(class_connect, 'DB_CONNECTION')

def test_should_be_has_equal_return(class_connect, link_conection) -> None:
    assert class_connect.DB_CONNECTION.__eq__(link_conection)

def test_should_be_return_session(class_connect) -> None:
    assert class_connect.session() is not None
