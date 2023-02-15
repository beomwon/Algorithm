def solution(spell, dic):
    return 1 if sorted(spell) in [sorted(v) for v in dic] else 2