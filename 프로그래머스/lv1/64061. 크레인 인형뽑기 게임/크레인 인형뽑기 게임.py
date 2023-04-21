def solution(board, moves):
    box, delete = [0], 0
    for i in moves:
        for j in range(len(board[1])):
            if board[j][i-1] != 0:
                if box[-1] == board[j][i-1]:
                    box.pop()
                    delete += 2
                else:
                    box.append(board[j][i-1])
                board[j][i-1] = 0
                break
    return delete