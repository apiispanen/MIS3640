def print_lyrics():
    print('Hey Jude.')
    print('Take a sad song')

print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print('Na - na - na - na - na, na - na - na - na')
    print_lyrics()

def print_twice(name):
    print(name)
    print(name)

print_twice('andrew')

#Give the absolute Value of X
def my_abs(x):
    print(abs(x))
my_abs(-2)


#Solve for x in 0 = ax**2+by+c
def quadratic(a, b, c): 
    X1 = ((-1*b + ((b**2)-4*a*c))**.5)/(2*a)
    X2 = ((-1*b + ((b**2)-4*a*c))**.5)/(2*a)
    return round(X1,3),round(X2,3)
    
print(quadratic(1,2,0))
