import time

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        time.sleep(1)
        countdown(n-1)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

#Factorial
def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)
#print(factorial(12))

#Fibonacci
