def solution(a, b):
    return int(str(a)+str(b)) if str(a)+str(b) > str(b)+str(a) else int(str(b)+str(a))