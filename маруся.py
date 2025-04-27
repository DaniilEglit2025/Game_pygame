for n in range(0, 21):
    if n > 20:
        i = n % 10
        if n == 0:
            n = 10
    else:
        i = n
    if n ==0:
        print('У вас 0 сообщений')
    elif n ==1:
        print('У вас 1 соообщение')
    elif i>=2 and i <=4:
        print('У вас ',n ,' сообщения')
    elif i >=5 and i <=20:
        print('У вас ',n ,' сообщений')
