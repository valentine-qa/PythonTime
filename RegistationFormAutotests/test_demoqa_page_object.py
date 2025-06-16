from selene import browser, by, have, command

from Lesson8_python.models.users import User
from Lesson9_PageObject.demoqa_page_object import resources
from RegistationFormAutotests.data.data import RegistrationPage


def test_demoqa(browser_params):
    registration_page = RegistrationPage()
    #Open page
    registration_page.open()

    registration_page.type_first_name('valentine')
    registration_page.type_last_name('borodich')
    registration_page.type_email('valentineqa@gmail.com')
    registration_page.choose_gender('Male')
    registration_page.type_number('4477217351')
    registration_page.fill_date_of_birth('2000', 'May', '13')
    registration_page.type_subject('Maths')
    registration_page.choose_hobby('Sports')
    registration_page.upload_user_picture('picture.png')
    registration_page.type_current_address('Minsk, Belarus')
    registration_page.choose_state("NCR")
    registration_page.choose_city("Delhi")
    registration_page.click_submit()

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