from itertools import permutations

def solution(k, dungeons):
    _max = 0
    for order in permutations(dungeons):
        fatigue = k
        for index, (least, cost) in enumerate(order):
            if least <= fatigue: fatigue -= cost
            else: _max = max(index, _max); break
        else:
            return len(dungeons)
        
    return _max