AI = int(input('Введите время:'))
if AI >=0 and AI <=5:
    print('Доброй ночи')
elif AI >=6 and AI <=11:
    print('Доброе утро')
elif AI >=12 and AI <=17:
    print('Добрый день')
elif AI >=18 and AI <=21:
    print('Добрый вечер')
elif AI >=22 and AI <= 23:
    print('Доброй ночи')
else:
    print('Неверное время')