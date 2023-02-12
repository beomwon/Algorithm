def solution(rsp):
    answer = ''
    for v in rsp:
        if v == '2': answer += '0'
        elif v == '0': answer += '5'
        else: answer += '2'
    return answer