def look_twice(x):
    print(x)
    print(x)
def cat_twice(part1, part2):
    cat=part1+part2
    look_twice(cat)

line1 = 'Tidde'
line2='Bang'
cat_twice(line1,line2)

import turtle

alex = turtle.Turtle()
print(alex)


#Create a Polygon
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

arc(alex,100,270)


turtle.mainloop()