def solution(i, j, k):
    return ''.join([str(n) for n in range(i,j+1)]).count(str(k))
    