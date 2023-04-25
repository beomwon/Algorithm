def solution(strArr):
    count = {k:0 for k in range(1,31)}
    for arr in strArr:
        count[len(arr)]+= 1
        
    return max(count.values())