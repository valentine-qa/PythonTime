import csv
from enum import Enum

from Lesson8_python.models.users import User, Status
import pytest

# -------------------------------------------------------------------
# Используем функциональный подход.
# Выносим логику в отдельные функции или фикстуры
# -------------------------------------------------------------------
USER_ADULT_AGE = 18


@pytest.fixture
def get_users() -> list[User]:
    with open("users.csv") as f:
        users_list = list(csv.DictReader(f, delimiter=";"))
    return [User(name=user["name"],
                 age=int(user["age"]),
                 status=Status(user["status"]),
                 items=user["items"])
            for user in users_list]

@pytest.fixture
def workers(get_users) -> list[User]:
    """
    Берем только работников из списка пользователей
    """
    workers = [user for user in get_users if user.status == Status.worker]
    return workers


def test_workers_are_adults_v2(workers):
    """
    Тестируем, что все работники старше 18 лет
    """
    for worker in workers:
        assert worker.is_adult(), f"Worker {worker.name} млдаше {USER_ADULT_AGE} лет"

