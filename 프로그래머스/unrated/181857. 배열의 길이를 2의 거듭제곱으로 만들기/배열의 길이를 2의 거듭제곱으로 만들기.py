def solution(arr):
    _len, t = len(arr), 0
    while True:
        if _len <= 2**t: break
        t += 1
    result = [0] * (2**t)
    result[:_len] = arr
    return result