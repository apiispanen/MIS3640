from mypolygon import square
import turtle
draw=turtle.Turtle()
t=turtle
square(draw,120)

#t.mainloop()

age = input("What is your age?")
age=int(age)
if age>=18:
    print("your age is {}.".format(age))
    print("Adult")
elif age<=6:
    print("sup kid, you're {}.".format(age))
else:
    print("your age is {}".format(age))
    print('Teenager')

    