def solution(w):
    answer = ''
    for v in w:
        if v.isupper():
            answer += v.lower()
        else:
            answer += v.upper()
    return answer