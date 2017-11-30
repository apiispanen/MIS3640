import math
def test_sqrt(x):
    original_x = x
    def mysqrt(x):
        return x**(1/2)
    print('a -- mysqrt(a) -- math.sqrt(a) --  diff')
    for i in range(1,original_x+1):
        print('{:.2f}   {:.2f}         {:.2f}           {:.2f}'. format(i,mysqrt(i),math.sqrt(i), (mysqrt(i)-math.sqrt(i))))

    
test_sqrt(10)