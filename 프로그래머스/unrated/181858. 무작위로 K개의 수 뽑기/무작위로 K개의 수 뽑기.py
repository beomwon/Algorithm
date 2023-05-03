def solution(arr, k):
    result, cur = [-1]*k, 0
    for v in arr:
        if v not in result:
            result[cur] = v
            cur += 1
        if -1 not in result:
            return result
    return result
        
    