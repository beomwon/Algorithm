def solution(dots):
    a = (dots[1][0] - dots[0][0]) / (dots[1][1] - dots[0][1])
    b = (dots[3][0] - dots[2][0]) / (dots[3][1] - dots[2][1])
    c = (dots[2][0] - dots[1][0]) / (dots[2][1] - dots[1][1])
    d = (dots[3][0] - dots[0][0]) / (dots[3][1] - dots[0][1])
    if a == b or c == d: return 1
    print(a,b,c,d)
    return 0