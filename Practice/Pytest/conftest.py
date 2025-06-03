import pytest

@pytest.fixture(scope="session")
def setup_session():
    print("\nSetting up for the entire test session")
    yield
    print("\nTearing down after the entire test session")