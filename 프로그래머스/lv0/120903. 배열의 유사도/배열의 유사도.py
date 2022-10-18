def solution(s1, s2):
    answer=0
    for v in s1:
        if v in s2:
            answer += 1
    return answer