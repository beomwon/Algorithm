def solution(my_string, index_list):
    answer = ''
    for v in index_list:
        answer += my_string[v]
    return answer