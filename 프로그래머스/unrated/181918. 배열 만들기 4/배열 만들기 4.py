def solution(arr):
    i, end, stk = 0, len(arr), []
    while i < end:
        if stk == [] or stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        else:
            stk.pop()
            
    return stk