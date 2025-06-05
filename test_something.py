import pytest
from selene import browser, be, have


@pytest.fixture()
def login_page(browser):
    print("login test")

@pytest.fixture()
def user():
    print("Юзер!")
    return "username", "password"


def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"
    assert 1 == 1

def test_logot(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"
    assert 1 == 1