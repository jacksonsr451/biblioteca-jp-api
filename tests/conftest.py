import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.orm import scoped_session, sessionmaker

from src.infrastructure.services.sqlalchemy_service import Base


@pytest.fixture(scope='session')
def connection(request):
    engine = create_engine('sqlite:///testdb.db')

    connection = engine.connect()

    def teardown():
        connection.close()

    request.addfinalizer(teardown)
    return connection


@pytest.fixture(scope='session', autouse=True)
def setup_db(connection, request):

    Base.metadata.bind = connection
    Base.metadata.create_all()

    def teardown():
        Base.metadata.drop_all()

    request.addfinalizer(teardown)


@pytest.fixture(autouse=True)
def session(connection, request):
    transaction = connection.begin()
    engine = create_engine('sqlite:///testdb.db')
    Session = scoped_session(sessionmaker(sessionmaker(bind=engine)))
    session = Session(bind=connection)
    session.begin_nested()

    @event.listens_for(session, 'after_transaction_end')
    def restart_savepoint(db_session, transaction):
        if transaction.nested and not transaction._parent.nested:
            session.expire_all()
            session.begin_nested()

    def teardown():
        Session.remove()
        transaction.rollback()

    request.addfinalizer(teardown)
    return session
