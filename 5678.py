from turtle import *
import random

setup(700,500)
speed(0)
for i in range(1,1000001):
    up()
    goto(random.randint(-300,300),random.randint(-200,200))
    down()
    circle(random.randint(50,200))
    begin_fill()

exitonclick()