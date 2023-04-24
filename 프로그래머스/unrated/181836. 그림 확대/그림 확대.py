def solution(picture, k):
    answer = []
    for v in [[''.join([c*k for c in list(p)])]*k for p in picture]: answer += v
    return answer