#BMI Calculator (Exercise 1)
def bmi_calc():
    height = input('What is your height (in)?')
    height= int(height)
    weight = input('What is your weight (lbs)?')
    weight = int(weight)
    bmi = 703*(weight/(height**2))
    print('Your bmi is {:.1f}'.format(int(bmi)))
    if bmi>=30:
        print("You're obese")
    elif bmi>=25:
        print("You still overweight")
    elif bmi>=18.5:
        print("You're normal")
    elif bmi<18.5:
        print("Eat something, you're underweight")

#bmi_calc()

#Factorial (Exercise 2)
def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)
#print(factorial(12))

#Fibonacci 
def fib(x):
    a=0
    b=0
    c=1
    for i in range(x):
        a=b
        b=c
        c=a+b
        print(c)
#fib(10)

#Greatest common denominator
import math
math.gcd

def gcd(a,b):
    d=0
    if a%2!=1 and b%2!=1:
        a = a/2
        b = b/2
        d = d + 1
    if a!=b:
        if a%2==0:
            a=a/2
        elif b%2==0:
            b=b/2
        elif a > b: 
            a=(a-b)/2
        else:
             b=(b-a)/2
    g=a
    print(g,d)

#gcd(16,8)

