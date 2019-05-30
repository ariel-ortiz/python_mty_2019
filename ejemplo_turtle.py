# Ariel Ortiz, 30 de mayo de 2019

from turtle import fd, rt, done, pencolor, pensize, ht, speed


def cuadrado(lado):
    for i in range(4):
        fd(lado)
        rt(90)

ht()
speed(0)
pencolor('#FF0000')
pensize(5)
for i in range(10):
    cuadrado(150)
    rt(36)
done()