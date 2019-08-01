import pytest

@pytest.fixture()
def setup1():
    print("\nSetup 1")
    yield
    print("\nTeardown 1")

@pytest.fixture()
def setup2(request):
    print("\nSetup 2")

    def teradown_a():
        print("\nTeardown A")

    def teardown_b():
        print("\nTeardown B")

    request.addfinalizer(teradown_a)
    request.addfinalizer(teardown_b)

def test1(setup1):
    print("Execute test1!")
    assert True

def test2(setup2):
    print("Executing test2!")
    assert True
