#Give the absolute Value of X
def my_abs(x):
    print(abs(x))

#Try it, fill in the blank!
my_abs(-3)


#Solve for x in 0 = ax**2+by+c
def quadratic(a, b, c): 

    X1 = ((-1*b + ((b**2)-4*a*c))**.5)/(2*a)
    X2 = ((-1*b + ((b**2)-4*a*c))**.5)/(2*a)
    if X1 ==complex:
        print ('no solution')
    else:
        print('X1 = %d,', format(round(X1,3),round(X2,3)))
    if X2 ==complex:
        print('noX2')
    else:
        print('X2 = %d', format(round(X2,3)))
#Try it
quadratic(1,3,-4)
