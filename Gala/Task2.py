def solution(V,R):
    #Store an array of all possible digits with bases of 0-36 
    digits = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #Divide the V by R and use the remainder to get the "one's" place of the result
    #V = str(V)
    #for digit in V:
     #   print(int(digit)*R)
    digits = digits[0:R]
    print(digits)
    
    A=[]
    x = 0
    while True:
        A.append(0)
        print(A) 
        if V/(R**x)<R:
            break
        else:
            x+=1
    
    length = len(A)
    print("the length is {}".format(length))

solution(16,15)
#16 7 = 22
    
    #D1=(V%R)]
    #D2=int((V-D1)/R)
    #D3=

    #V1=digits[D1]
    #V2=digits[D2]
    #V3=digits[D3]

    #print(D3,D2,D1)
    #print("{}{}".format(V2,V1))

