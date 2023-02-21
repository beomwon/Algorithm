def solution(n):
    fibo = [0,1]
    
    for i in range(1, n):
        fibo.append(sum(fibo[-2:]))
        
    return fibo[-1]%1234567