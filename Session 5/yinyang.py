#!/usr/bin/env python3

from turtle import *

def yin(radius):
    width(3)
    circle(radius/2., 180)
    circle(radius, 180)
    left(180)
    circle(-radius/2., 180)
    left(90)
    up()
    forward(radius*0.35)
    right(90)
    down()
    circle(radius*0.15)
    left(90)
    up()
    backward(radius*0.35)
    down()
    left(90)

def main():
    reset()
    yin(200)
    yin(200)
    ht()
    


main()
mainloop()