import os
import time

import pytest
from selene import browser, by, have, be

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

    browser.element('#genterWrapper').element(by.text("Male")).click()
    browser.element('#userNumber').type('4477217351')

    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").element("[value='4']").click()
    browser.element(".react-datepicker__year-select").element("[value='2000']").click()
    browser.all(".react-datepicker__day:not(.react-datepicker__day--outside-month)").element_by(have.text('13')).click()

    browser.element('#subjectsInput').set_value('Maths').press_enter()
    browser.element('#currentAddress').type('Minsk, Belarus')

    browser.element("#hobbiesWrapper").element("label[for=hobbies-checkbox-1]").click()
    browser.element('input[id=uploadPicture]').send_keys(os.path.abspath('picture.png'))

    browser.element('#state').click()
    browser.element("#stateCity-wrapper").element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element("#stateCity-wrapper").element(by.text("Delhi")).click()

    browser.element("#submit").click()

    browser.element(".modal-content").should(be.visible)
    browser.element(".modal-content").should(have.text("Thanks for submitting the form"))
    browser.all(".table-responsive").element_by(have.exact_texts("Student Name", "valentine"))