def solution(num_list):
    answer = [0,0]
    for v in num_list:
        if v%2 == 0: answer[0] += 1
        else: answer[1] += 1 
    return answer