def solution(my_str, n):
    answer = []
    while True:
        answer.append(my_str[:min(n,len(my_str))])
        my_str = my_str[n:]
        if len(my_str) == 0:
            break
    return answer