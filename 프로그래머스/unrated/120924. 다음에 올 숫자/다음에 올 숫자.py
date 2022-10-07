def solution(c):
    if (c[0] - c[1]) == (c[1] - c[2]): return c[-1] - (c[0] - c[1])
    else: return c[-1] / (c[0]/c[1])