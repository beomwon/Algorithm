def solution(s):
    result = [0, 0]
    while s != '1':
        result = [result[0] + 1, result[1] + s.count('0')]
        s = bin(len(s.replace('0', '')))[2:]
        
    return result