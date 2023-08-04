def solution(triangle):
    if len(triangle) == 1:
        return triangle[0]
    
    _max = triangle[-1]
    for i in range(len(triangle)-2, -1, -1):
        temp = []
        for t, v in enumerate(triangle[i]):
            temp.append(max(_max[t:t+2])+v)
        _max = temp
        
    return temp[0]