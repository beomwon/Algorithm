from collections import deque

def solution(numbers, k):
    numbers = deque(numbers)
    numbers.rotate(-2*(k-1))
    return numbers[0]