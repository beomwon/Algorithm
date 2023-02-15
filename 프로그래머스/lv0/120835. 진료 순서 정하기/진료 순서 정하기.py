def solution(emergency):
    rank = sorted(emergency, reverse=True)
    return [rank.index(e)+1 for e in emergency]