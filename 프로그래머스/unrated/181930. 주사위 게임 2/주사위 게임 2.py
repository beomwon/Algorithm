def solution(a, b, c):
    return (a+b+c)*(1 if len(set([a,b,c]))==3 else a**2+b**2+c**2)*(1 if len(set([a,b,c]))!=1 else a**3+b**3+c**3)