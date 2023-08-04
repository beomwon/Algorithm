def solution(n):
    answer = [[0 if x!=y else 1 for x in range(n)] for y in range(n)]
    return answer