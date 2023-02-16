def solution(n):
    result = []
    divide_num = 2
    while n!=1:
        if n%divide_num == 0:
            n/= divide_num
            result.append(divide_num)
        else:
            divide_num += 1
        
    return sorted(set(result))