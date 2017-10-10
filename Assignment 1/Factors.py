def factor(n):
    #Housekeeping--> Make sure the numbers entered are integers and above zero. 
    if not int(n)==n and n>=0:
        print("Positive and whole number please.")
    #Run a loop that stops at the number divided by any number up to itself.
    #If the remainder of dividing the original number by the tested number, print that number.
    for i in range(1, n + 1):
        if n % i == 0:
           print(i)