login = input('Введите логин')
password = input('Введите пароль')

if login == 'admin' and password == 'a777aa':
    print('Добро пожаловать в Пентогон')
else:
    if login == 'admin':
        print('Неверный пароль')
    else:
        print('Неверный логин')