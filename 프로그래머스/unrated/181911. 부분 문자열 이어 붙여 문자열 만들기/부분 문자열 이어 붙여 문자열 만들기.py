def solution(my_strings, parts):
    answer = ''
    for word, size in zip(my_strings, parts):
        answer += word[size[0]: size[1]+1]
    return answer