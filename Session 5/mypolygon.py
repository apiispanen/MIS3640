import turtle
t=turtle.Turtle()
#Create a Polygon
def square(t, length):
    for i in range(4):
        t.fd(length)    
        t.lt(360/4)


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)    
        t.lt(360/n)
#polygon(alex, 3, 10)

import math

def circle(t,r):
    circumference = 2*math.pi * r
    n = 50
    length = circumference/n
    polygon(t,length,n)

#circle(alex, 80)


def arc(t, r, angle):
    arc_length = 2*math.pi *r*angle / 360
    n = int(arc_length /3) +1
    step_length =arc_length /n
    step_angle = angle/n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_length)
