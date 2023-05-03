def solution(l, r):
    answer = []
    for i in range(l,r+1):
        if str(i).replace('5','').replace('0','') == '':
            answer.append(i)
            
    return answer if len(answer) else [-1]