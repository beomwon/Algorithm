def solution(s):
    answer = ''
    for v in s:
        if s.count(v) == 1: answer += v
    return ''.join(sorted(answer))
