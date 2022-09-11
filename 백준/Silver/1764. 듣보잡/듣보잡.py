import sys

n,m=map(int,input().split())
temp, res = {}, []

for _ in range(n):
    dummy = sys.stdin.readline().strip()
    temp[dummy] = dummy

for _ in range(m):
    dummy = sys.stdin.readline().strip()
    try:
        res.append(temp[dummy])
    except:
        pass

print(len(res))
for v in sorted(res):
    print(v)