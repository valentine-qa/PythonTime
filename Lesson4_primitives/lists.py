l = [1, 2, 3, 'a', 'b', 'c', [4, 5, 6]]

print(l[-1]) #[4, 5, 6]
print(l[-1][1]) # 5
print(l[::-1]) #[[4, 5, 6], 'c', 'b', 'a', 3, 2, 1]

#Функции списков

l.append('borodulkin')
l.append(['aas', 'asd'])
print(l)
print(len(l))
l.reverse()
print(l)
l[0] = 200
print(l)

#Множества

s1 = {1, 2, 3, 4, 5, 1, 2}
s2 = {1, 2, 3, 3}
print(s1) #Нет дубликатов
print(s2) #Нет дубликатов
print(s1.intersection(s2))

print(s1-s2) #{4, 5}
print(list(set([1, 2, 3, 4, 5, 5, 6]))) #уникализация списка (делаем множество и обратно)
