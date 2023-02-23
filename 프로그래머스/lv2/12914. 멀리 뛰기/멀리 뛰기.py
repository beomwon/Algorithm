def solution(n):
    if n == 1: return 1

    answer = [1, 2]
    for i in range(2, n):
        answer.append(sum(answer[-2:]))
    return answer[-1]%1234567