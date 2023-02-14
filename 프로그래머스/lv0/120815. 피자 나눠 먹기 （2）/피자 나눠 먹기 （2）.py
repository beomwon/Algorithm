def solution(n):
    for i in range(1, n*6):
        if 6*i % n == 0:
            return i