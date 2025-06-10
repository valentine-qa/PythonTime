s = "Hello, world!"
s = 'Hello, world!'
s = '''Hello "World"'''
s = '''Hello 
"Wo
rld"'''
print(s)

#Иднексы и слайсы

email = 'valentine-qa@mail.com'
print(email[0]) #v
print(email[0:5]) #valen
print(email[:5]) #valen
print(email[-2:-5])
print(email[::-1]) #moc.liam@aq-enitnelav

#Операции
print(email.find('l'))
print(len(email))
print(email)
print(email.capitalize())
assert email.endswith('@mail.com')

#Форматирование
a = 'borodulkin'
b = 'valentine'

print(a + ' ' + b) #borodulkin valentine
print("{a}, bababa {b}".format(a = a, b = b)) #borodulkin, bababa valentine
print(f"{a}, berbebe {b}") #borodulkin, berbebe valentine
print(f"{a}, berbebe {b.upper()}") #borodulkin, berbebe VALENTINE
print(f"{a=}, berbebe {b=}") #a='borodulkin', berbebe b='valentine'

url_template = "https://ya.ru/{}" #https://ya.ru/{}
users_url = url_template.format("abc") #https://ya.ru/abc
groups_url = url_template.format("bca") #https://ya.ru/bca
print(url_template, users_url, groups_url)

#Сроку в число и наоборот

s = "1234"
n = 1234

assert s == str(n)
assert  int(s) == n