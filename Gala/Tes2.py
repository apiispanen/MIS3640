def solution(V, R):
    digits="0123456789abcdefghijklmnopqrstuvwxyz"
    if V==0:
        return 0

    A = V // R

    if A == 0:
        return digits[V%R]
    else:
        return solution(A,R)+digits[V%R]

print(solution(17,7))
print(solution(62,21))
print()
print(16%2)
print(14//3)
print(17//5)
print(100//33)