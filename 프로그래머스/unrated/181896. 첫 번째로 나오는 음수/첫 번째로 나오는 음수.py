def solution(num_list):
    for i, v in enumerate(num_list):
        if v < 0:
            return i 
    return -1