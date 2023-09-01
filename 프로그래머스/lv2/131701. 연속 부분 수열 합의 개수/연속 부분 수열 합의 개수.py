def solution(arr):
    end = len(arr)
    arr += arr
    answer = []
    for i in range(1, end+1):
        window = sum(arr[:i])
        answer.append(window)
        for j in range(i, len(arr)):
            window = window - arr[j-i] + arr[j]
            answer.append(window)
    
    return len(set(answer))
        
        
