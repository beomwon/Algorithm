def solution(balls, share):

    a=1
    b=1
    c=0
    for i in range(balls, 0 , -1) :
        a = a * i
        c +=1
        if c == share :
            break
    for i in range(share, 0, -1) :
        b = b * i




    answer = a//b
    return answer