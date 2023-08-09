def solution(arr):
    answer = [0, 0, 0]
    while len(arr) != 1:
        _next = [[[0] for _ in range(len(arr)//2)] for _ in range(len(arr)//2)]
        for i in range(0, len(arr), 2):
            for j in range(0, len(arr), 2):
                _sum = [arr[i][j], arr[i+1][j], arr[i][j+1], arr[i+1][j+1]]
                if len(set(_sum)) != 1:
                    answer[0] += _sum.count(0)
                    answer[1] += _sum.count(1)
                    _next[i//2][j//2] = 2
                else:
                    _next[i//2][j//2] = _sum[0]
        arr = _next.copy()
        
    answer[arr[0][0]] += 1
    return answer[:2]