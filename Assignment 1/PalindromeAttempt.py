def isPalindrome(s):
    #If the length is equal to 1 or 0 then we know it cannot be simplified further and is a palindrome.
    if s[0]==s[-1] and len(s)>1:    #shorten the word and compare the next 2 ourside letters.
        isPalindrome(s[1:-1])
    elif s[0]!=s[-1]:
        return False
    else:
        return True 
inputStr = input("Enter a string: ")
#Lowercase the letters to standardize them when we match them.
inputStr=inputStr.lower()
if isPalindrome(inputStr):
    print("That's a palindrome.")
else:
    print("That isn't a palindrome. Nice Try.")
