def solution(arr):
    stk, i= [], -1
    while (i:=i+1) < len(arr):
        if len(stk):
            if stk[-1] == arr[i]: stk.pop()
            else: stk.append(arr[i])
        else:
            stk.append(arr[i])
            
    return stk if len(stk) else [-1]