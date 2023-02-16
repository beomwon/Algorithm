def solution(board):
    board = [[0 for _ in range(len(board[0])+2)]] + [[0] + v + [0] for v in board] + [[0 for _ in range(len(board[0])+2)]]
    result = 0
    for y in range(1, len(board)-1):
        for x in range(1, len(board[0])-1):
            safe = True
            if board[y][x] == 0:
                for check_y in range(y-1,y+2):
                    if sum(board[check_y][x-1:x+2]) != 0:
                        safe = False
                if safe:
                    result += 1
                    
    return result