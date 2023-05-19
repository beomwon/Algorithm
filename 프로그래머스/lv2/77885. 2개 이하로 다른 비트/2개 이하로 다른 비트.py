def solution(numbers):
    answer = []
    for num in numbers:
        r = bin(num)[2:][::-1] + '0'
        i, v = len(r), None
        
        for b in ['00','10','01']:
            if b in r and r.index(b) < i:
                i, v = r.index(b), b
                
        change = {'00':'10', '10':'01', '01':'11'} 
        r = r.replace(v, change[v], 1)[::-1]
        answer.append(int(r,2))
            
    return answer

# 00 -> 01
# 01 -> 10
# 10 -> 11

# 00 -> 10
# 10 -> 01
# 01 -> 11



