def solution(arr, queries):
    for s,e,k in queries:
        arr = [v+1 if (s<=i<=e and i%k ==0) else v for i, v in enumerate(arr)]
            
    return arr