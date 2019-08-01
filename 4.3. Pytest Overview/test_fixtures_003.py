import pytest

@pytest.fixture(autouse=True)
def setup():
    print("\nSetup")

def test1():
    print("Execute test1!")
    assert True

def test2():
    print("Executing test2!")
    assert True

