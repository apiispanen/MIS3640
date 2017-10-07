
def solution(A):
    if len(A)==0:
        return -1
    else:
        M=sum(A)/len(A)
        dev =[]
        for P in A: 
            deviate = (abs(P - M))
            dev.append(deviate)
        return(dev.index(max(dev)))

A = [9,4,-3,-10]

print(solution(A))
