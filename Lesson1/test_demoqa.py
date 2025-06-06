import time

import pytest
from selene import browser


@pytest.fixture(scope="function")
def browser_params():
    browser.config.hold_browser_open = True
    browser.config.window_width = 1280
    browser.config.window_height = 800
    browser.config.driver_name = 'chrome'

    yield
    time.sleep(4)
    browser.quit()

def test_demoqa(browser_params):


    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('valentine')
    browser.element('#lastName').type('borodich')
    browser.element('#userEmail').type('valentineqa@gmail.com')
    browser.element('#currentAddress').type('Minsk, Belarus')
    browser.element('#userNumber').type('447721735')
