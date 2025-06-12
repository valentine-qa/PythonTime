import time

import pytest
from selene import browser, be, have


@pytest.fixture()
def preconditions():
    browser.config.hold_browser_open = True
    browser.config.window_width = 1280
    browser.config.window_height = 800
    browser.config.driver_name = 'chrome'

    yield

    time.sleep(4)
    browser.quit()

def test_form(preconditions):
    browser.open('https://frutonyanya.ru/register/')

    browser.element('[name=name]').type('Валентин')
    browser.element('[name=email]').type('valen111tine@gmail.com')
    browser.element('[name=tel]').type('9889312560')
    browser.element('[name=password1]').type('valen123')
    browser.element('[name=password2]').type('valen123')
    browser.element('button[type=submit]').press_enter()

    browser.element('.popup_good').should(be.visible)
    browser.element('.popup_good .popup__title').should(have.text('Спасибо!'))
