def solution(V,R):
    #Store an array of all possible digits with bases of 0-36 
    digits = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    digits = digits[0:R]
    print(digits)
    print(int(V/R))

    print(V%R)

solution(16,4)
#16 4  = 100
#62 21 = 2k
  
  #  D1=(V%R)
   # D2=int((V-D1)/R)
    #if D2>=R:
     #   D2=V%(R-D1)
      #  D3=V%(R-D2)
    #else:
     #   pass
        

    #V1=digits[D1]
    #V2=digits[D2]
    #V3=digits[D3]

    #print(D3,D2,D1)
    #print("{}{}".format(V2,V1))