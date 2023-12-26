from collections import deque

# 그룹, 방문 여부, 그룹 넘버 변수
group, visited = {}, {}
group_count = 0
n, m = 0, 0
DIR = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # 이동 방향 정의

def bfs(sx, sy, visited, group, land):

    #너비 우선 탐색을 통해 그룹을 찾아내고 그룹의 크기를 계산

    global group_count, n, m
    count = 1
    q = deque([(sx, sy)])
    visited[(sx, sy)] = group_count

    while q:
        x, y = q.popleft()

        for dx, dy in DIR:
            nx, ny = x + dx, y + dy

            # 유효한 범위 내에 있고, 석유가 들었고 방문하지 않았다면 추가
            if 0 <= nx < n and 0 <= ny < m and land[nx][ny] != 0 and (nx, ny) not in visited:
                visited[(nx, ny)] = group_count
                q.append((nx, ny))
                count += 1

    group[group_count] = count
    group_count += 1


def solution(land):
    global n, m
    n, m = len(land), len(land[0])

    # 모든 지점을 탐색하면서 그룹을 찾음
    for row in range(n):
        for col in range(m):
            if (row, col) not in visited and land[row][col] != 0:
                bfs(row, col, visited, group, land)

    maximum = 0

    # 각 열에 대해 최대 그룹 크기를 계산
    for col in range(m):
        already_gone = {}
        ret = 0

        for row in range(n):
            if land[row][col] != 0:
                cur_group = visited[(row, col)]

                # 이미 계산한 그룹이면 skip
                if cur_group in already_gone:
                    continue

                cur_count = group[cur_group]
                ret += cur_count
                already_gone[cur_group] = True

        maximum = max(maximum, ret)

    return maximum

# def solution(land):
#     n, m = len(land), len(land[0])
#     land = [land[i]+[0] for i in range(n)] + [[0 for _ in range(m+1)]]
#     check = [[-1 for _ in range(m+1)] for _ in range(n+1)]
#     oil_weights = []
#     for y in range(n):
#         for x in range(m):
#             if land[y][x] == 1:
#                 if check[y][x] != -1:
#                     oil_weights[check[y][x]] += 1
#                 else:
#                     check[y][x] = len(oil_weights)
#                     oil_weights.append(1)
                
#                 if land[y][x+1] == 1:
#                     check[y][x+1] = check[y][x]
#                 if land[y+1][x] == 1:
#                     check[y+1][x] = check[y][x]
                    
#     line_weights = [[] for _ in range(m)]
#     total = [0 for _ in range(m)]
#     for x in range(m):
#         for y in range(n):
#             if check[y][x] != -1 and check[y][x] not in line_weights[x]:
#                 line_weights[x].append(check[y][x])
#                 total[x] += oil_weights[check[y][x]]
                
#     return max(total)