from itertools import combinations
def solution(number):
    return list(map(sum,list(combinations(number,3)))).count(0)