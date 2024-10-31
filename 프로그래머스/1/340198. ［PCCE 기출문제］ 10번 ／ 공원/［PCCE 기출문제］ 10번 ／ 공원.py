def solution(mats, park):
    mats.sort(reverse=True)
    n, m = len(park), len(park[0])

    def can_place(size, x, y):
        if x + size > n or y + size > m:
            return False
        for i in range(x, x + size):
            for j in range(y, y + size):
                if park[i][j] != '-1':
                    return False
        return True

    for size in mats:
        for i in range(n):
            for j in range(m):
                if can_place(size, i, j):
                    return size
    return -1