def solution(sizes):
    w, h = 0, 0
    for s in sizes:
        w = max(max(s), w)
        h = max(min(s), h)
    return w*h