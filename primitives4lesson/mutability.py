# Списки, словари и множества - изменяемы!

from copy import deepcopy #для полного копирования списка и т.д

l1 = [1, 2, 3]
l2 = l1
l2.append(4) #Операция модифицирует один и тот же список, а не делает копию!!!!!
print(l1, l2) #[1, 2, 3, 4] [1, 2, 3, 4]
l3 = l2
l3.append(5)
print(l1, l2, l3) #[1, 2, 3, 4, 5] [1, 2, 3, 4, 5] [1, 2, 3, 4, 5]

l11 = [1, 2, 3]
l21 = l11.copy() #Создает копию списка! (для полного копирования будет deepcopy())
l21.append(44)
print(l11, l21) #[1, 2, 3] [1, 2, 3, 44]

# Кортежи, frozenset - не изменяем

t = (1, 2, 3, 4, 5)
print(t[:3])
# t[1] = 123 #error, нельзя менять содержимоем, можем просто узнавать инфу
t2 = t #а тут уже создает новый а не ссылается т.к. он неизменяем

frozenset({1, 2, 3, 4, 5, 6, 1})
print(frozenset)