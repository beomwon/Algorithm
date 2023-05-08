temp = ['0','1','2','3','4','5','6','7','8','9']

def convert(n, k):
    q, r = divmod(n, k)
    if q == 0 :
        return temp[r] 
    else :
        return convert(q, k) + temp[r]
    
def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        
    return True

def solution(n, k):
    return sum([isPrime(int(v)) for v in convert(n,k).split('0') if v not in ['','1']])