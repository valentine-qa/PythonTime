import pytest
from selene import browser, have

@pytest.fixture(scope="module") #or scope="function"
def open_browser():
    browser.config.window_width = 1280
    browser.config.window_height = 800
    browser.open('https://ya.ru/')
    browser.element('input[name="text"]').type('selene').press_enter()

    yield

    browser.quit()

def test_search(open_browser):
    browser.element('#search-result').should(have.text('yashaka/selene'))

def test_search2(open_browser):
    browser.element('#search-result').should(have.no.text('asdasdasd'))