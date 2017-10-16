AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
numbers = [42, 123]
empty = []
print(AFC_east, numbers, empty)

AFC_east[3]='Green Bay Packers'

print('')

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    
]

print (L[-1][-1])

numbers = [2, 0, 1, 6, 9]

#for i in range(len(numbers)):
 #   numbers[i] = numbers[i] * 2
new_numbers = [number * 2 for number in numbers]  
print(new_numbers)


my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]
print(len(my_list))

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print ([0] * 4)
t = ['a', 'b', 'c', 'd', 'e', 'f']
t.insert(2, 'winfred')
print(t) #prints b and c (NOT D BECAUSE IT IS NOT INCLUSIVE)

import numpy as np
a=np.array(a)
print(a)
print(a*2)


AFC_west = AFC_east.copy()

print (AFC_west)

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res
#Mapping moves or "Maps" elements into a sequence (above)
#Reduce reduces the array into one element (Sum, average)

print(len(AFC_east))

print('a'<'b')
