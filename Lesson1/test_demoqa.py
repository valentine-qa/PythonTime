import os
import time

import pytest
from selene import browser, by, have, be, command




def test_demoqa(browser_params):

    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('valentine')
    browser.element('#lastName').type('borodich')
    browser.element('#userEmail').type('valentineqa@gmail.com')

    # browser.element('#genterWrapper').element(by.text("Male")).click()
    # browser.all('[name=gender]').element_by(have.value('Male')).click()
    # browser.element('[name=gender][value=Male]').click()
    browser.all('[for^=gender-radio]').element_by(have.text('Male')).click()
    # browser.element('[name=gender]').element('..').click()
    browser.element('#userNumber').type('4477217351')

    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").element("[value='4']").click()
    browser.element(".react-datepicker__year-select").element("[value='2000']").click()
    browser.all(".react-datepicker__day:not(.react-datepicker__day--outside-month)").element_by(have.text('13')).click()

    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('#currentAddress').type('Minsk, Belarus')

    # browser.element("#hobbiesWrapper").element("label[for=hobbies-checkbox-1]").click()
    browser.element("#hobbiesWrapper [for=hobbies-checkbox-1]").click()
    browser.element('input[id=uploadPicture]').send_keys(os.path.abspath('../RegistationFormAutotests/picture.png'))

    browser.element('#state').click()
    # browser.element("#stateCity-wrapper").element('#react-select-3-option-0').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
    browser.element('#city').click()
    browser.element("#stateCity-wrapper").element(by.text("Delhi")).click()

    browser.element("#submit").click()
    browser.element("#submit").perform(command.js.click) #Js click если перекрывается футером

    browser.element(".modal-content").should(be.visible)
    browser.element(".modal-header").should(have.text("Thanks for submitting the form"))
    browser.element(".modal-body").should(have.text('Student Name').and_(have.text('valentineqa@gmail.com')))
    # browser.element(".modal-body").should(have.texts('Student Name', 'valentineqa@gmail.com'))