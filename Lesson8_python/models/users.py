from dataclasses import dataclass
from enum import Enum

USER_ADULT_AGE = 18

class Status(Enum):
    student = "student"
    worker = "worker"


@dataclass
class User:
    name: str
    age: int
    status: Status
    items: list[str]

    def is_adult(self):
        return self.age >= USER_ADULT_AGE


class Worker(User):

    status = Status.worker

    def __init__(self, name, age, items):
        self.name = name
        self.age = age
        self.items = items



    # def __init__(self, name, age, status, items):
    #     self.name = name
    #     self.age = age
    #     self.status = status
    #     self.items = items


if __name__ == '__main__':

    d = {"name": "Oleg", "age": 16, "status": "student", "items": ["book", "pen", "paper"]}

    oleg = User(name="Oleg", age=16, status=Status.student, items=["book", "pen", "paper"])
    oleg2 = User(name="Oleg", age=16, status=Status.worker, items=["book", "pen", "paper"])

    olga_worker = Worker(name="Olga", age=16, items=["book", "pen", "paper"])

    assert  oleg == oleg2

