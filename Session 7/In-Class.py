import math
import astropy.table
def test_sqrt(x):
    def mysqrt(x):
        return x**(1/2)
    print('a  mysqrt(a)   math.sqrt(a)   diff   ')
    for i in range(x):
        print(i,mysqrt(i),math.sqrt(i), (mysqrt(i)-math.sqrt(i)))

    
test_sqrt(10)