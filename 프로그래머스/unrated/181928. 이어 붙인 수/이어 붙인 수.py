def solution(num_list):
    return int(''.join([str(i) for i in num_list if i%2])) + int(''.join([str(i) for i in num_list if not(i%2)]))