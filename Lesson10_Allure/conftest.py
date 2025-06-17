import time

import pytest
from selene import browser


@pytest.fixture(scope="function")
def browser_params():
    browser.config.hold_browser_open = True
    browser.config.window_width = 1600
    browser.config.window_height = 800
    browser.config.driver_name = 'chrome'

    yield

    time.sleep(4)
    browser.quit()