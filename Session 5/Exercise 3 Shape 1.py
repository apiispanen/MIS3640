import turtle
import math
draw = turtle.Turtle()
print(draw)
#Create a Polygon
#def polygon(t, length, n):
 #   for i in range(n):
  #      t.fd(length)    
   #     t.lt(360/n)
#polygon(alex, 3, 10)

t = turtle 

#First Circle
t.circle(100)

#Weird Shape
t.home()
t.left(90)
t.fd(200)
t.rt(120)
t.fd(100)
t.rt(120)
t.fd(200)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(30)
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(200)
t.rt(120)
t.fd(100)
t.rt(120)
t.fd(100)
#Circle Time
t.rt(180)
t.fd(50)
t.circle(29)
t.rt(180)
t.fd(100)
t.circle(29)
t.rt(180)
t.fd(50)
t.lt(90)
t.fd(50)
t.circle(29)
t.rt(180)
t.fd(100)
t.circle(29)
#Not the best looking thing, but it's close!


t.mainloop()