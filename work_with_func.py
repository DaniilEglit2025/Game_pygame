import random
spec = {'firework':10000,'heal':1000,'food':2000}#ЭТО СЛОВАРЬ
stuff = ['laser','firework','heal','food','bait']#ЭТО СПИСОК

#в данной функции используется ИМЕНОВАННЫЙ АРГУМЕНТ: stuff = None
#это значит что в этой функции мы всегда ожидаем некий набор вещей который мы называем стафф
#но, название набора вещей до функции может быть каким угодно, именованный аргумент задаёт как бы правило
#что на вход функции ждём набор вещей
def damage(stuff,spec):
    if stuff and spec is not None:
        for predmet in stuff:
            if predmet in spec:
                print(predmet, '-', spec[predmet])



def hp(stuff,spec):
    for predmet in stuff:
        if predmet in spec:
            print(predmet, '-', spec[predmet])

damage(stuff[random.randint(0,4):random.randint(0,7)],spec)
hp(stuff[random.randint(0,4):random.randint(0,7)],spec)
#def foo(*args):
#    for i in args:
#        print(i)
#
#foo("name", 3, [1,2], {"key":2}, "asdfasdfsdf")
#
#print("###############################")
#
#def bar(**kwargs):
#    for i in kwargs.values():
#        print(i)
#
#В данном случае мы выводим и ключ и значение словаря,
#используя метод словаря items()
#    for k, v 
#
#
#bar(name="name", chislo=3, spisok=[1,2])
#
#print("#############################")
#
#def foo_bar(*args, **kwargs):
#    for i in args:
#        print(i)
#
#    for k, v in kwargs,items():
#        print(k, ':',v)
#foo_bar("adsdasdf", 123, name="Nik", age=29)