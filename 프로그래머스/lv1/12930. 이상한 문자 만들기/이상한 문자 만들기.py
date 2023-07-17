def solution(s):
    i, ans = 0, ''
    
    for w in s:
        if i%2 == 0: ans += w.upper()
        else: ans += w.lower()
        i = i + 1 if w != ' ' else 0
        
    return ans