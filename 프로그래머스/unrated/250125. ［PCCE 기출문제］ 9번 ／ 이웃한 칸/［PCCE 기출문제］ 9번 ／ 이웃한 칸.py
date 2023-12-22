def solution(board, h, w):
    b = [['1'] * (len(board)+2)] + [['1']+board[i]+['1'] for i in range(len(board))] + [['1'] * (len(board)+2)]
    c = b[h+1][w+1]
    answer = int(b[h][w+1] == c) + int(b[h+1][w] == c) + int(b[h+2][w+1] == c) + int(b[h+1][w+2] == c)    
    return answer