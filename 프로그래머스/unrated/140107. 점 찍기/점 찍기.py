def solution(k, d):
    answer, basket = 0, [(i*k)**2 for i in range(d+1) if (i*k)**2 <= d**2]
    cur, index = 0, len(basket)-1
    while True:
        while basket[cur] + basket[index] > d**2: 
            index-= 1
            if index < 0:
                return answer
            
        answer += index+1
        cur += 1
        if cur > len(basket)-1:
            return answer