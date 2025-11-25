import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.settings import Settings
from app.db.base import Base
from app.db.session import get_db
from app.main import app


@pytest.fixture(scope="function")
def test_settings():
    """Override settings with test database URL"""
    test_db_url = "sqlite:///./test.db"
    settings = Settings(
        APP_NAME="test_company_website",
        ENV="test",
        DATABASE_URL=test_db_url,
    )
    return settings


@pytest.fixture(scope="function")
def test_db(test_settings):
    """Create test database and session"""
    engine = create_engine(
        test_settings.DATABASE_URL, connect_args={"check_same_thread": False}
    )
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestingSessionLocal
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client(test_db):
    """Create test client"""
    return TestClient(app)

