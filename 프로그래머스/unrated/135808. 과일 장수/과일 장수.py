def solution(k, m, score):
    score.sort(reverse=True)
    return sum([score[target]*m for target in range(m-1, len(score), m)])