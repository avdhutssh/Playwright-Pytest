import pytest


@pytest.fixture(scope="function")
def setup_function():
    print("\nSetting up for a function test in test_Demo2.py")
    yield
    print("\nTearing down after a function test in test_Demo2.py")

def test_example3(setup_function, setup_session):
    print("\nRunning test_example3")
    assert True

def test_example4(setup_function):
    print("\nRunning test_example4")
    assert True