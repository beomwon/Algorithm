def solution(my_string, m, c):
    return ''.join([v for i, v in enumerate(my_string[c-1:]) if i%m==0])