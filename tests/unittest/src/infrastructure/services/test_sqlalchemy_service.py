from src.infrastructure.services import sqlalchemy_service


def test_should_be_has_base_metadata() -> None:
    assert hasattr(sqlalchemy_service, 'Base')

def test_should_be_is_not_none() -> None:
    assert sqlalchemy_service.Base is not None
