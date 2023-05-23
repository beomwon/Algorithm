def solution(t):
    missiles, end = 0, 0
    
    for s, e in sorted(t):
        if end <= s:
            missiles += 1
            end = e
        else: 
            end =  min(end, e)

    return missiles