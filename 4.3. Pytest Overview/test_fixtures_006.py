import pytest

@pytest.fixture(params=[1, 2, 3])
def setup(request):
    reVal = request.param
    print("\nSetup!   retVal = {}".format(reVal))
    return reVal

def test1(setup):
    print("\nsetup = {}".format(setup))
    assert True
