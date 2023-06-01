def solution(arr):
    answer = [v for v in arr.replace('a','.').replace('b','.').replace('c','.').split('.') if v != '']
    return answer if answer else ['EMPTY']