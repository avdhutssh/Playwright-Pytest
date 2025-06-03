import pytest


@pytest.fixture(scope="module")
def setup_module():
    print("\nSetting up for a module test")
    yield
    print("\nTearing down after a module test")

@pytest.fixture(scope="function")
def setup_function():
    print("\nSetting up for a function test")
    yield
    print("\nTearing down after a function test")

@pytest.fixture(scope="function")
def setup_functionSpecific():
    print("\nSetting up for a Specific function test")
    yield
    print("\nTearing down after a Specific function test")

def test_example1(setup_module,  setup_function, setup_session):
    print("\nRunning test_example1")
    assert True

def test_example2(setup_module, setup_function, setup_functionSpecific):
    print("\nRunning test_example2")
    assert True