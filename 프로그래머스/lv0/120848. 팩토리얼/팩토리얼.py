def solution(n):
    fac = 1
    for i in range(2, 10):
        fac *= i
        if fac == n: return i
        elif fac > n: return i-1 
    return 10