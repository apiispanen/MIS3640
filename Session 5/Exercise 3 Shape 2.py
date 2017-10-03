import turtle
import math
draw = turtle.Turtle()
print(draw)

t = turtle
t.circle(100)

t.lt(90)
def arc(x, r, angle):
    arc_length = 2*math.pi *r*angle / 360
    n = int(arc_length /3)+1
    step_length =arc_length /n
    step_angle = angle/n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_length)

arc(t,500,15)


t.mainloop()