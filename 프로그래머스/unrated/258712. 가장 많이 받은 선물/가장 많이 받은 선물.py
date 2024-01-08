def solution(friends, gifts):
    history = {name: {'friends': {k: 0 for k in friends}, 'score': 0} for name in friends}
    next_month_gift = {name: 0 for name in friends}
    
    for gift in gifts:
        give, get = gift.split()
        
        history[give]['friends'][get] += 1
        history[give]['score'] += 1
        
        history[get]['friends'][give] -= 1
        history[get]['score'] -= 1
    
    for name in history.keys():
        for fname, fscore in history[name]['friends'].items():
            if fscore > 0 or (fscore == 0 and history[name]['score'] > history[fname]['score']):
                next_month_gift[name] += 1

    return max(next_month_gift.values())