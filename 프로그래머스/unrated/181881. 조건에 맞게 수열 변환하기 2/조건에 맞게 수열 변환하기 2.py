def solution(arr):
    _cur = arr.copy()
    result = 0
    while True:
        _next = _cur.copy()
        for i, v in enumerate(_cur):
            if 50 <= v and v%2 == 0: _next[i] = v%2
            if v < 50 and v%2 == 1: _next[i] = v*2 + 1
        if _next == _cur:
            return result
        else:
            _cur = _next.copy()
            result += 1