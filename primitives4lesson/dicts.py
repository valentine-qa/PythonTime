#Словари

d = {
    "k": "valentine",
    'k2': "borodulkin"
}

user1 = {
    "name": "Vasya",
    "age": 18
}

user2 = {
    "name": "valentine",
    "age": 20,
    "id": 25
}
print(user1)
print(user2)

print(user1["name"])
print(user2["age"])

users = {
    25: user1,
    42: user2
}
print(users[42])

#Функции
from pprint import pprint
print('------------')
print(users.items())
print('------------')
pprint(list(users.items()))
print('------------')
print(users)
print(users.keys())
print(users.get(100), {"name": "empty user"}) #Не будет ошибки если нет элемента
print(users[42]) #Будет ошибка если такого элемента не будет
users[55] = {
    "name": "borodulkin",
    "age": 20,
    "id": 25
} #Можно положить значение
print(users)

def test_hueta():
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = {}
    for item in zip(first, second):
        d.update(item)
        print(d)