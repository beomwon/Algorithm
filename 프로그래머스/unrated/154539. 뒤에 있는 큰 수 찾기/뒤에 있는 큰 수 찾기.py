def solution(ns):
    ans, check = [-1]*len(ns), [] 
    for i, v in enumerate(ns):
        while check and ns[check[-1]] < v:
            ans[check.pop()] = v
        check += [i]
        
    return ans