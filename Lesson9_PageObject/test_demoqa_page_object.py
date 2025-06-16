import time

import pytest
from selene import browser, by, have, be, command

from Lesson8_python.models.users import User
from Lesson9_PageObject.demoqa_page_object import resources

class RegistrationPage:

    def __init__(self):
        self.registered_user_data = browser.element('.table').all('td').even


    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def type_first_name(self, name):
        browser.element('#firstName').type(f'{name}')
    def type_last_name(self, last_name):
        browser.element('#lastName').type(f'{last_name}')
    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").type(month)
        browser.element(".react-datepicker__year-select").type(year)
        browser.all(".react-datepicker__day:not(.react-datepicker__day--outside-month)").element_by(
            have.text(day)).click()

    def should_have_registered_user_with(self, full_name, user_mail, user_gender, user_number, user_birth,
                                         user_subject, user_hobby, user_picture, user_address,
                                         user_city):
        browser.element(".modal-content").should(be.visible)
        browser.element(".modal-header").should(have.text("Thanks for submitting the form"))
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{full_name}',
                f'{user_mail}',
                f'{user_gender}',
                f'{user_number}',
                f'{user_birth}',
                f'{user_subject}',
                f'{user_hobby}',
                f'{user_picture}',
                f'{user_address}',
                f'{user_city}'
            )
        )





def test_demoqa(browser_params):
    registration_page = RegistrationPage()
    #Open page
    registration_page.open()
    user = User(first_name='valentine', last_name='borodich')
    registration_page.type_first_name('valentine')
    registration_page.type_last_name('borodich')

    browser.element('#userEmail').type('valentineqa@gmail.com')

    browser.element('#genterWrapper').element(by.text("Male")).click()
    # browser.all('[name=gender]').element_by(have.value('Male')).click()
    # browser.element('[name=gender][value=Male]').click()
    # browser.all('[for^=gender-radio]').element_by(have.text('Male')).click()
    # browser.element('[name=gender]').element('..').click()
    browser.element('#userNumber').type('4477217351')

    registration_page.fill_date_of_birth('2000', 'May', '13')

    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('#currentAddress').type('Minsk, Belarus')

    # browser.element("#hobbiesWrapper").element("label[for=hobbies-checkbox-1]").click()
    browser.element("#hobbiesWrapper [for=hobbies-checkbox-1]").click()
    browser.element('input[id=uploadPicture]').send_keys(resources.img_path('../RegistationFormAutotests/picture.png'))

    browser.element('#state').click()
    # browser.element("#stateCity-wrapper").element('#react-select-3-option-0').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
    browser.element('#city').click()
    browser.element("#stateCity-wrapper").element(by.text("Delhi")).click()

    # browser.element("#submit").click()
    browser.element("#submit").perform(command.js.click) #Js click если перекрывается футером


    registration_page.should_have_registered_user_with(
        'valentine borodich',
        'valentineqa@gmail.com',
        'Male',
        '4477217351',
        '13 May,2000',
        'Maths',
        'Sports',
        'picture.png',
        'Minsk, Belarus',
        'NCR Delhi'
    )