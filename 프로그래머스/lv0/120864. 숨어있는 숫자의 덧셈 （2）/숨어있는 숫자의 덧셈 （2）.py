def solution(my_string):
    answer = []
    n = ''
    for v in my_string:
        if v.isdigit():
            n += v
        else:
            if n != '':
                answer.append(int(n))
                n = ''
    if n != '':
        answer.append(int(n))
        
    return sum(answer)