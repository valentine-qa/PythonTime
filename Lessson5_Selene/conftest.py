from sys import executable

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='module')
def browser_managment():
    browser.config.driver_name = 'chrome' #Простяцкий варик

    # Продвинутый варик (без запуска браузера)!!!!! (более чем достаточно)
    # driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless')
    # browser.config.driver_options = driver_options

    #Самостоятельное создание драйвера, который перекрывает selene
    # driver_options = webdriver.ChromeOptions()
    # browser.config.driver = webdriver.Chrome(
    #     service=ChromeService(executable_path=ChromeDriverManager().install()),
    #     options=driver_options,
    # )

    browser.config.base_url = "https://todomvc.com/examples/emberjs/"
    browser.config.window_width = 1980
    browser.config.window_height = 1280

    yield

    browser.quit()