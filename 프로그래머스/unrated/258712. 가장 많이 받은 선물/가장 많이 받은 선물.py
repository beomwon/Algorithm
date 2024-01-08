def solution(friends, gifts):
    gift_info = {name: {'friends': {k: 0 for k in friends}, 'score': 0, 'total': 0} for name in friends}
    for gift in gifts:
        give, get = gift.split()
        
        gift_info[give]['friends'][get] += 1
        gift_info[give]['score'] += 1
        
        gift_info[get]['friends'][give] -= 1
        gift_info[get]['score'] -= 1
    
    for name in gift_info.keys():
        for friend_name, friend_score in gift_info[name]['friends'].items():
            if friend_score > 0 or (friend_score == 0 and gift_info[name]['score'] > gift_info[friend_name]['score']):
                print(name, friend_name)
                gift_info[name]['total'] += 1
    
    answer = 0
    for k, v in gift_info.items():
        answer = max(answer, v['total'])
    
    print(gift_info)
        
    return answer