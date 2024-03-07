n, m = map(int, input().split())
basket = [0 for _ in range(n)]
for _ in range(m):
    start, end, number = map(int, input().split())
    basket[start-1: end] = [number] * (end-start+1)

print(*basket)