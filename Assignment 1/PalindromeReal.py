def isPalindrome(s):
    #note: this is a test with recursion!!

    
    #Lowercase the letters to standardize them when we match them.
    i=0
    new_word=''
    for letter in s.lower():
        new_word="{}{}".format(new_word,s.lower()[-1-i])
        i+=1   
    if new_word == s.lower():
        return True
    else:
        return False
    print (new_word)
inputStr = input("Enter a string: ")
if isPalindrome(inputStr):
    print("That's a palindrome.")
else:
    print("That isn't a palindrome. Nice Try.")
