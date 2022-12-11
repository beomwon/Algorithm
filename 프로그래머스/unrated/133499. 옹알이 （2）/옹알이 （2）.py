def solution(babbling):
    able = ['aya', 'ye', 'woo', 'ma']
    answer = []
    count = 0
    for v in babbling:
        flag = True
        for a in able:
            if a*2 in v:
                flag = False
                break
        if flag: answer.append(v)
    
    for v in answer:
        v = v.replace('aya','A').replace('ye','Y').replace('woo','W').replace('ma','M')
        v = v.replace('A','').replace('Y','').replace('W','').replace('M','')
        # print(v)
        if v == '': count += 1
        
    return count