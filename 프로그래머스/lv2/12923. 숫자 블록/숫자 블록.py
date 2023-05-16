def solution(s, e):
    answer = []
    if s == 1:
        answer.append(0)
        s = s + 1
        
    for i in range(s, e+1):
        n, isadd = [1], True
        for d in range(2, min(int(i**0.5)+1, 10000000)):
            if i%d == 0:
                n.append(d)
                if i/d <= 10000000:
                    answer.append(int(i/d))
                    isadd = False
                    break
        if isadd:
            answer.append(n[-1])
            
    return answer