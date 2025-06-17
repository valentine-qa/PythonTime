from re import S

from selene import browser, by, be

#Для получения отчета в консоли   allure serve Lesson10_Allure/allure-results
def test_browser(browser_params):

    browser.open('https://github.com/')


    browser.element('.search-input').click()
    browser.element('#query-builder-test').type("eroshenkoam/allure-example").press_enter()
    browser.element(by.link_text("eroshenkoam/allure-example")).click()
    browser.element('#pull-requests-tab').click()
    browser.element(by.partial_text('#91')).should(be.visible)