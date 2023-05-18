def solution(a, d, included):
    return sum([a+d*i for i,v in enumerate(included) if v])