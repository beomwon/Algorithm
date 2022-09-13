start, end = map(int,input().split())
min_ = end+1


def make(v, c):
    global min_
    if v == end:
        if min_ > c:
            min_ = c
        return
    if v > end:
        return
    make(v*2, c+1)
    make(v*10+1, c+1)

make(start, 1)

print(min_ if min_!=end+1 else -1)