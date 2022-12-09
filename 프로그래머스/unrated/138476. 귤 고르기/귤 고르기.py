from collections import Counter

def solution(k, tangerine):
    answer = 0
    sum = 0
    tan = Counter(tangerine).most_common()
    
    for t in tan:
        sum += t[1]
        answer += 1
        if sum >= k:
            return answer
    
    return answer