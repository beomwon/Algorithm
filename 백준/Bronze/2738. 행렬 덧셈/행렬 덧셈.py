m, n = map(int, input().split())
numbers = [0] * (n*m)
for _ in range(2):
    for y in range(m):
        for x, value in enumerate(input().split()):
            numbers[y*n + x] += int(value)

for _ in range(m):
    print(*numbers[:n])
    numbers = numbers[n:]