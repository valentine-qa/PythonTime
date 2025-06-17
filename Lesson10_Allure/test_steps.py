from re import S

import allure
from selene import browser, by, be

#Для получения отчета в консоли   allure serve Lesson10_Allure/allure-results
def test_dinamic_steps(browser_params):
    with allure.step("Открываем главную страницу"):
        browser.open('https://github.com/')

    with allure.step('Ищем репозиторий'):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').type("eroshenkoam/allure-example").press_enter()
    with allure.step('Переходим пол ссылке репозитория'):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step('Открываем таб Pull Requests'):
        browser.element('#pull-requests-tab').click()
    with allure.step('Проверяес наличие реквеста с номером 91'):
        browser.element(by.partial_text('#91')).should(be.visible)

def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_pull_tab()
    should_see_issue_with_number('#91')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com/')

@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    browser.element('.search-input').click()
    browser.element('#query-builder-test').type(repo).press_enter()

@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()

@allure.step('Открываем таб Pull Requests')
def open_pull_tab():
    browser.element('#pull-requests-tab').click()

@allure.step('Ищем  Pull Request с номером {number}')
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).should(be.visible)