def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    for target in range(m-1, len(score), m):
        answer += score[target]*m
    return answer