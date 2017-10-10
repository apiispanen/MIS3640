def nested_sum(t):
    """Computes the total of all numbers in a list of lists.

    t: list of list of numbers

    returns: number

    Expected output:
    21
    """
    a=[]
    for element in x:
        a.append(sum(element))
#    print(sum(a))

x = [[1, 2], [3], [4, 5, 6]]
nested_sum(x)



def cumsum(t):
    a=[]
    p=0
    for element in t:
       a.append(element+sum(t[0:p]))
       p+=1
#    print(a)

t = [1, 2, 3]
cumsum(t)
#[1, 3, 6]
"""Computes the cumulative sum of the numbers in t.

    t: list of numbers

    returns: list of numbers

    Expected output

    """
    



def middle(t):
    """Returns all but the first and last elements of t.

    t: list

    returns: new list

    Expected output:
    """
    return t[1:-1]
t = [1, 2, 3, 4]
#print(middle(t))
    #[2, 3]


def chop(t):
    """Removes the first and last elements of t.

    t: list

    returns: None

    Expected output:
        """
    t=t[1:-1]
    return t
t = [1, 2, 3, 4]
#print(chop(t))
#[2, 3]


def is_sorted(t):
    """Checks whether a list is sorted.

    t: list

    returns: boolean

    Expected output:
   """
    if isinstance(t[0],int):
        prev=0
    else:    
        prev=''
    dp=prev
    for element in t:
        if (element>prev or element==prev) and (prev>dp or prev==dp):
           return True
        else:
            return False
        prev=element
        dp=prev
#is_sorted([1, 2, 2])
#    True
#is_sorted(['b', 'a'])
#    False

def is_anagram(word1, word2):
    """Checks whether two words are anagrams

    Two words are anagrams if you can rearrange the letters from one to 
    spell the other.

    word1: string or list
    word2: string or list

    returns: boolean
Expected output:
    """
    return sorted(word1)==sorted(word2)
is_anagram('stop', 'pots')
#True
is_anagram('different', 'letters')
#False
is_anagram([1, 2, 2], [2, 1, 2])
#Ture
    
    

def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.

    s: string or list

    returns: bool

    output:

    """
    # if there is any letter in s, then it is True. Otherwise, False
    for letter in s:
        if any(letter): 
            return True
        else:
            return False
print(has_duplicates('cba'))
#False
print(has_duplicates('abba'))
#True
    

def has_adjacent_duplicates(s):
    a=""
    b="-"
    for letter in s:
        if s[0]==letter:
            break 
        if (b==a and letter>a) or (letter==a and a>b):#it's previous one 
            return True
        b=a
        a=letter
        
    """Returns True if there are two same adjacent elements.
    
    s: string or list

    returns: bool

    """

 # if there is any letter in s, then it is True. Otherwise, False
    


print(has_adjacent_duplicates('cba'))
    #False
print(has_adjacent_duplicates('abca'))
    #Flase
print(has_adjacent_duplicates('abbc'))
    #True
    

def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    t = [1, 2, 3]
    print(cumsum(t))

    t = [1, 2, 3, 4]
    print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))


if __name__ == '__main__':
    main()