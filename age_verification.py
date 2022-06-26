
# проверка возраста
age = input('Введите ваш возраст: ')

# алтернативные условия
# if 18 <= int(age) <= 55:
# if int(age) >= 18 and int(age) <= 55:

if age == 'admin' or int(age) >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

print('Конец программы...')