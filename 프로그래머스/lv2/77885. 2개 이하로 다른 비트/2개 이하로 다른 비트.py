def solution(numbers):
    answer = []
    for num in numbers:
        r = ('0'+bin(num)[2:])[::-1]
        found = {'index': len(r), 'what': None}
        
        for before in ['00','10','01']:
            if before in r and r.index(before) < found['index']:
                found = {'index': r.index(before), 'what': before}
                
        change = {'00':'10', '10':'01', '01':'11'} 
        r = r.replace(found['what'], change[found['what']], 1)
        
        # if r[-1] == '0': r = r[:-1]
        answer.append(int(r[::-1],2))
            
    return answer

# 00 -> 01
# 01 -> 10
# 10 -> 11

# 00 -> 10
# 10 -> 01
# 01 -> 11



