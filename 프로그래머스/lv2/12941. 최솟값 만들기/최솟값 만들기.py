def solution(A,B):
    A, B = sorted(A, reverse=True), sorted(B)
    return sum([x*y for x,y in zip(A,B)])