speed1 = int(input('Введите скорость:'))
speed2 = int(input('Введите скорость:'))
speed3 = int(input('Введите скорость:'))
if speed1 > speed2 and speed1 > speed3:
    print('Скорость speed1 самая большая')
elif speed2 > speed1 and speed2 > speed3:
    print('Скорость speed2 самая большая')
else:
    print('Скорость speed3 самая большая')
