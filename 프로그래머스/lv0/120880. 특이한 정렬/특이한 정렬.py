def solution(numlist, n):
    rank = sorted([[value, distance:=abs(value-n)] for value in numlist], key = lambda x: (x[1],-x[0]))
    return [v[0] for v in rank]