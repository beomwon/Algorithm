def solution(order):
    return sum([1 for w in str(order) if w in ['3','6','9']])