def solution(arr):
    length = max(len(arr[0]), len(arr))
    answer = [[0]*length for i in range(length)]
    
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            answer[y][x] = arr[y][x]
            
    return answer