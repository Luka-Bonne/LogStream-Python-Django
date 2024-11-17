import pytest


@pytest.fixture(autouse=True)
def my_fixture():
    with open('test.txt', "w") as f:
        pass