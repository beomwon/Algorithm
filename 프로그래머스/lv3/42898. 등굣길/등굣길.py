# def solution(m, n, puddles):
#     maps = [[0] * m for _ in range(n)]
#     maps[0][0] = 1
#     puddles = [[y-1,x-1] for y, x in puddles]
#     for y in range(n):
#         for x in range(m):
#             if [y, x] not in puddles:
#                 if y+1 < n and [y+1, x] not in puddles: maps[y+1][x] += maps[y][x]
#                 if x+1 < m and [y, x+1] not in puddles: maps[y][x+1] += maps[y][x]
#     print(maps)
#     return maps[-1][-1] % 1000000007


def solution(m, n, puddles):
    grid = [[0]*(m+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0 or [j, i] in puddles:
                grid[i][j] = 0
            elif i == 1 and j == 1:
                grid[i][j] = 1
            else:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return (grid[n][m] % 1000000007)