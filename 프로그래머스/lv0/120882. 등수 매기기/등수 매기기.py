def solution(score):
    total = sorted([sum(s) for s in score]+[201], reverse=True)
    return [total.index(sum(v)) for v in score]