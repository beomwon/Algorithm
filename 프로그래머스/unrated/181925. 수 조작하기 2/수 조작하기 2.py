def solution(l):
    answer = ''
    control = {1:'w', -1:'s', 10:'d', -10:'a'}
    for i in range(len(l)-1):
        answer += control[l[i+1]-l[i]]
        
    return answer