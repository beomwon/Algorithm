def solution(dirs):
    visited = [[0 for _ in range(21)] for _ in range(21)]
    op = {'U':[2, 0], 'D':[-2, 0], 'R':[0, 2], 'L':[0, -2]}
    px, py = 10, 10
    
    for move in dirs:
        mx, my = op[move]
        print(move, end=' ')
        if 0<= px+mx <= 20 and 0<= py+my <= 20:
            print(px, py ,'in')
            px += mx
            py += my
            visited[px+(-mx//2)][py+(-my//2)] = 1
    return sum([sum(v) for v in visited])