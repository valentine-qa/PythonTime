import csv

import pytest


# -------------------------------------------------------------------
# Используем функциональный подход.
# Выносим логику в отдельные функции или фикстуры
# -------------------------------------------------------------------

@pytest.fixture
def users():
    with open("users.csv") as f:
        users = list(csv.DictReader(f, delimiter=";"))
    return users

@pytest.fixture
def workers(users):
    """
    Берем только работников из списка пользователей
    """
    workers = [user for user in users if user['status'] == 'worker']
    return workers


def test_workers_are_adults_v2(workers):
    """
    Тестируем, что все работники старше 18 лет
    """
    for worker in workers:
        assert int(worker["age"]) >= 18, f"worker {worker["name"]} ne sovershennoletni"