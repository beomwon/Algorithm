def solution(p, l):
    p.sort()
    ans, front, end = 0, 0, len(p)-1
    
    while front < end:
        if p[front] + p[end] <= l: front += 1
        end -= 1
        ans += 1
            
    return ans + int(front == end)
