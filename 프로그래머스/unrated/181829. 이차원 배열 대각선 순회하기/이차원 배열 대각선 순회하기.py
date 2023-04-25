def solution(board, k):
    answer = 0
    for i in range(len(board)):
        j = 0
        while i+j <= k and j<len(board[0]):
            answer += board[i][j]
            j+=1
            
    return answer