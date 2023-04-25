def solution(numbers, n):
    answer = 0
    for v in numbers:
        answer += v
        if answer > n:
            return answer