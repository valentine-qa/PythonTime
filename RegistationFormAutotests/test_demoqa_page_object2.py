from selene import browser, by, have, command

from Lesson6_Python.loops import user_number
from RegistationFormAutotests.data.data import User
from Lesson9_PageObject.demoqa_page_object import resources
from RegistationFormAutotests.data.data import RegistrationPage


def test_demoqa(browser_params):
    registration_page = RegistrationPage()
    valentine = User(first_name='valentine',
                     last_name='borodich',
                     user_email='valentineqa@gmail.com',
                     user_gender='Male',
                     user_phone='4477217351',
                     user_birthday_day='13',
                     user_birthday_year='2000',
                     user_birthday_month='May',
                     user_subject='Maths',
                     user_hobby='Sports',
                     user_picture='picture.png',
                     user_city='Delhi',
                     user_state='NCR',
                     user_current_address='Minsk, Belarus',
                     )
    #Open page
    registration_page.open()

    registration_page.type_first_name(valentine.first_name)
    registration_page.type_last_name(valentine.last_name)
    registration_page.type_email(valentine.user_email)
    registration_page.choose_gender(valentine.user_gender)
    registration_page.type_number(valentine.user_phone)
    registration_page.fill_date_of_birth(valentine.user_birthday_year, valentine.user_birthday_month, valentine.user_birthday_day)

    registration_page.type_subject(valentine.user_subject)
    registration_page.choose_hobby(valentine.user_hobby)
    registration_page.upload_user_picture(valentine.user_picture)

    registration_page.type_current_address(valentine.user_current_address)
    registration_page.choose_state(valentine.user_state)
    registration_page.choose_city(valentine.user_city)
    registration_page.click_submit()

    registration_page.should_have_registered_user_with(
        f'{valentine.first_name} {valentine.last_name}',
        valentine.user_email,
        valentine.user_gender,
        valentine.user_phone,
        f'{valentine.user_birthday_day} {valentine.user_birthday_month},{valentine.user_birthday_year}',
        valentine.user_subject,
        valentine.user_hobby,
        valentine.user_picture,
        valentine.user_current_address,
        f'{valentine.user_state} {valentine.user_city}'
    )