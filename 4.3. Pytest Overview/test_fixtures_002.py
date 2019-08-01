import pytest

@pytest.fixture()
def setup():
    print("\nSetup")

def test1(setup):
    print("Execute test1!")
    assert True

@pytest.mark.usefixtures("setup")
def test2():
    print("Executing test2!")
    assert True

