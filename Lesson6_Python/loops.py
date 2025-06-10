import random
from pprint import pprint

from selene.core.query import value

#While

required_number = 7
user_number = random.randint(0, 10)

while required_number != user_number:
    user_number = random.randint(0, 10)
    print(f"Пользователь ввел {user_number}")

i = 10
while i != 0:
    print(i)
    i = i - 1

#For

users = [
    {"name": "Oleg", "age": 32},
    {"name": "Valya", "age": 25},
    {"name": "Inna", "age": 26},
    {"name": "Dima", "age": 48},
]

for user in users:
    print(user)
    print(f"Пользователю {user['name']}, {user['age']} лет")


d = {
    "first": 1,
    "sec": 2,
    "third": 3,
}

for key, value in d.items():
    print(f"Ключ {key}, значение {value}")

for i in range(0, 10):
    print(i)

cities = ["Minsk", "Slutsk", "Brest"]
for i, city in enumerate(cities):
    print(f"{city} na {i + 1} meste")