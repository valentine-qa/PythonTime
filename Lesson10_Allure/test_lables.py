import allure
from allure_commons.types import Severity


#Для получения отчета в консоли   allure serve Lesson10_Allure/allure-results
#Отчет смотреть во кладке Behaviors
def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозиториях")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link('https://github.com/', name="Testing")
    pass



@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", 'valentine-qa')
@allure.feature('"Задачи в репозиториях"')
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link('https://github.com/')
def test_decorator_labels():
    pass