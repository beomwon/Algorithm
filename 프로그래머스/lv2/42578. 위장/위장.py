def solution(clothes):
    _dict = {k:[] for _,k in clothes}
    for v, k in clothes:
        _dict[k].append(v)
    res = 1
    for v in _dict.values():
        res *= (len(v) + 1)
    return res - 1