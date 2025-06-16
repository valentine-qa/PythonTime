import dataclasses
import os

from selene import browser, be, have, by, command


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    user_gender: str
    user_phone: str
    user_birthdate: str
    user_subject: str
    user_hobby: str
    user_picture: str
    user_current_address: str
    user_city: str
    user_state: str


class RegistrationPage:

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def type_first_name(self, name):
        browser.element('#firstName').type(f'{name}')

    def type_last_name(self, last_name):
        browser.element('#lastName').type(f'{last_name}')

    def type_email(self, user_email):
        browser.element('#userEmail').type(f'{user_email}')

    def choose_gender(self, user_gender):
        browser.element('#genterWrapper').element(by.text(f'{user_gender}')).click()

    def type_number(self, user_number):
        browser.element('#userNumber').type(f'{user_number}')

    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").type(month)
        browser.element(".react-datepicker__year-select").type(year)
        browser.all(".react-datepicker__day:not(.react-datepicker__day--outside-month)").element_by(
            have.text(day)).click()

    def type_subject(self, user_subject):
        browser.element('#subjectsInput').type(f'{user_subject}').press_enter()

    def choose_hobby(self, user_hobby):
        browser.element("#hobbiesWrapper").element(by.text(f'{user_hobby}')).element('..').click()

    def upload_user_picture(self, user_picture):
        browser.element('input[id=uploadPicture]').send_keys(os.path.abspath(f'{user_picture}'))

    def type_current_address(self, user_current_address):
        browser.element('#currentAddress').type(f'{user_current_address}')

    def choose_state(self, user_state):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(f'{user_state}')).click()

    def choose_city(self, user_city):
        browser.element('#city').click()
        browser.element("#stateCity-wrapper").element(by.text(f"{user_city}")).click()

    def click_submit(self):
        browser.element("#submit").perform(command.js.click)



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














