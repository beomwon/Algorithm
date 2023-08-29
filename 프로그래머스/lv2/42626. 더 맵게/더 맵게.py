import heapq

def solution(s, k):
    heapq.heapify(s)
    answer = 0
    while s[0] < k:
        if len(s) == 1: 
            return -1
        heapq.heappush(s, heapq.heappop(s) + heapq.heappop(s)*2)
        answer += 1
    return answer