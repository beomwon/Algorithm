def solution(topping):
    ans, front, end = 0, {}, {}
    for t in topping:
        end[t] = end.get(t, 0) + 1
    for t in topping:
        end[t] -= 1
        front[t] = 1
        if end[t] == 0: del end[t]
        ans += len(front.keys()) == len(end.keys())
    
    return ans