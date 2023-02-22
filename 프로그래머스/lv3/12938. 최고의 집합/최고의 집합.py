def solution(n, s):
    if n>s:
        return [-1]
    
    share = s//n
    remainder = s%n
    
    return sorted([share + 1 if (remainder:= remainder-1)>=0 else share for _ in range(n)])