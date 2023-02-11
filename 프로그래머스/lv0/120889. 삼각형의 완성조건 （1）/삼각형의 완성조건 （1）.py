def solution(sides):
    sides.sort()
    return 1 if sum(sides[:2]) > sides[-1] else 2