from selene import browser, be, have

def test_yaru():
    browser.open('https://faros.ru/')
    # browser.element('[id="text"]').should(be.blank).type('selene').press_enter()
    # # browser.element('html').should(have.text('About this page'))
    # browser.element('#search-result').should(have.text('yashaka/selene'))

    browser.element('.table-menu .menu-item:nth-of-type(2)').click()
    browser.element('.table-menu .menu-item:nth-of-type(2)').click()
