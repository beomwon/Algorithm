def solution(n):
    answer = [0, 1, 1]
    for i in range(1, n):
        answer.append(sum(answer[-2:]))
    return answer[-1]%1234567