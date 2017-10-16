names = ['Julian', 'Zach', 'Alex']
scores = [95, 75, 85]

grades = {'Zach':75, 'Alex':85, 'Julian':95}

grades['Xiang']=88

#print(grades[''])
#KEY ERROR= Object referenced to is NOT a part of the original list
p = print 
p('Zach' in grades)

s='aabbbbcccdddeeee'
letters=[0,0,0,0,0]
for letter in s:
    if letter=='a':
        letters[0]+=1
    elif letter=='d':
        letters[3]+=1

p(letters)

#def histogram(s):
   # d = dict()
  #  for c in s.lower():
       # if c not in d:
       #     d[c] = 1
    #    else:
            #d[c] += 1
    #return d


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

