def solution(a, b, n):
    count = 0
    while True:
        if n - a < 0: break
        n = n - a + b
        count += b
        
    return count