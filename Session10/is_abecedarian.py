def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

#1
def is_a_resursed(word):
   
    if len(word)==1:
        return True
    else:
        return is_a_resursed(word[:-1]) and word[-2] < word[-1]

print(is_a_resursed('abcdef'))


#2
def while_ab(word):
    if len(word)==1:
        return False
    else:
        while not word[:-1]>word[-1]:
            return True
        else:  
            return False
print(while_ab('asf'))


