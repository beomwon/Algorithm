p = []
for i in range(int(input())):
    p.append(list(map(int, input().split())))
    
for i in range(1, len(p)):
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
    
print(min(p[-1][0], p[-1][1], p[-1][2]))