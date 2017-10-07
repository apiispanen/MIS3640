fin=open('words.txt')
def find_long_words():
    for word in fin:
        if len(word)>20:
            print(word)
        
#find_long_words()

def no_e(word):
    #for letter in word:
      #  if letter.lower() =='e':
     #       return False
    #return True
    return not 'e' in word.lower()


#print(no_e('suprior'))

def find_no_e_words():
    fin=open('words.txt')
    counter_no_e = 0
    counter_total=0
    for line in fin:
        counter_total+=1
        word=line.strip()
        if no_e(word):
            #print(word)
            counter_no_e +=1
    total = counter_no_e/counter_total*100
    print('Percentage of words with no "e" is {:.2f}%'.format(total))
#find_no_e_words()

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True
print(avoids('aaa', 'abcdefghijklmnopqrstuvwxyz'))



def find_no_vowel_words():
    fin=open('words.txt')
    counter_no_vowels = 0
    counter_total=0
    for line in fin:
        counter_total+=1
        word=line.strip()
        if avoids(word,'aeiou'):
            print(word)
            counter_no_vowels +=1
    total = counter_no_vowels/counter_total*100
    print('Percentage of words with no "e" is {:.2f}%'.format(total))
find_no_vowel_words()


#4
