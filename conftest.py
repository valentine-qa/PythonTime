import pytest


@pytest.fixture(scope="session")
def browser():
    print("open browser")

    yield

    print("close browser")