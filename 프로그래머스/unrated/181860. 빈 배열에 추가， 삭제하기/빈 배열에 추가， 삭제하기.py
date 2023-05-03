def solution(arr, flag):
    x = []
    for a, f in zip(arr, flag):
        if f:
            x += [a]*a*2
        else:
            for _ in range(a):
                x = x[:-1]
    return x