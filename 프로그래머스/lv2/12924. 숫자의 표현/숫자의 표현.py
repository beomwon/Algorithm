def solution(n):
    answer = 1
    
    for v in range(n-1, 0, -1):
        total = 0
        for d in range(v, 0, -1):
            total += d
            if total == n: 
                answer += 1
                break
            elif total > n: break
    return answer