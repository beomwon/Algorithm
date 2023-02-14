def solution(my_string):
    temp = []
    answer = ''
    for v in my_string:
        if v in temp:
            continue
        else:
            temp.append(v)
            answer += v
    return answer