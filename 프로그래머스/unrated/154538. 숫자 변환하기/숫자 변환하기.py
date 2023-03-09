def solution(x, y, n):
    calc = [[y,0]]
    while calc:
        compare, answer = calc.pop(0)
        if compare == x:
            return answer
        
        if compare > x:
            if compare%2==0:
                calc.append([compare/2, answer+1])
            if compare%3==0:
                calc.append([compare/3, answer+1])
            calc.append([compare-n, answer+1])
            
    return -1