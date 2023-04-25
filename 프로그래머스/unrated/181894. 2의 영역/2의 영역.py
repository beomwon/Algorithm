def solution(arr):
    t = [i for i in range(len(arr)) if arr[i]==2]
    
    if len(t) == 0: return [-1]
    elif len(t) == 1: return [2]
    else: return arr[t[0]:t[-1]+1]
        
        