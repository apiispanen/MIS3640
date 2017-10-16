#Exercise 1

def histogram(s):
    d = dict()
    for c in s.lower():
        d[c]=d.get(c,0)+1
    
    return d

h=histogram('The quick brown fox jumps over the lazy dog')

def print_hist():
    for c in h:
        print(c,h[c])

print_hist()

#Exercise 2
#Fibonacci Count
#Fibonacci 

def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


known = {1: 1, 2: 2}


def fib_efficient(n):
    global numFibCalls
    numFibCalls += 1
    if n in known:
        return known[n]
    else:
        ans = fib_efficient(n - 1) + fib_efficient(n - 2)
        known[n] = ans
        return ans


numFibCalls = 0
fibArg = 10

print(fib(fibArg))
print('function calls', numFibCalls)

numFibCalls = 0


print(fib_efficient(fibArg))
print('function calls', numFibCalls)
#fib(10)

#Exercise 3
#Global variables alllow for ease-of-acess use outside of the functions. It enables the variables to be carried out as flags for other functions for comparative purposes. 

#Exercise 4
#Write a function that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.
d = dict()
def word_keys():
    fin=open('words.txt')
    global d
    counter_total=0
    for line in fin:
        counter_total+=1
        word=line.strip()
        d[word]=counter_total
def check(word):
    global d 
    word=word.lower
    if word in d:
        print('Yes')
    else:
        print('no')

word_keys()

#Write a function named has_duplicates that takes a list as a parameter and returns True if there is any object that appears more than once in the list.

def has_duplicates(xlist):
    for item in xlist:
        xlist = xlist[1:len(xlist)]
        if item in xlist:
            print('A duplicate is: ',item)

a=[1,2,3,4,5,6,5,4,5,6,7,8]
has_duplicates(a)