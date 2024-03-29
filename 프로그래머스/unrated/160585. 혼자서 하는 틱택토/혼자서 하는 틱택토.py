def solution(b):
    o, x = sum([arr.count('O') for arr in b]), sum([arr.count('X') for arr in b])
    if 0 <= o-x <= 1:
        rb = [b[0][i]+b[1][i]+b[2][i] for i in range(3)]
        winO, winX = 0, 0
        for i, j in zip(b, rb):
            if 'OOO' in [i,j]: winO += 1
            if 'XXX' in [i,j]: winX += 1
        
        diagonal = [b[0][0] + b[1][1] + b[2][2], b[0][2] + b[1][1] + b[2][0]]
        winO += diagonal.count('OOO')
        winX += diagonal.count('XXX')
        
        if winX and winO: return 0
        if winO and winX == 0 and o==x: return 0
        if winX and winO == 0 and o!=x: return 0
        
        return 1
    
    return 0
                
    # O의 개수-X의 개수=0 or 1
    # O가 이겼다면 O의 개수는 X보다 한 개 많음.
    # X가 이겼다면 O의 개수와 X의 개수는 같음.
    # O와 X는 동시에 이길 수 없음.