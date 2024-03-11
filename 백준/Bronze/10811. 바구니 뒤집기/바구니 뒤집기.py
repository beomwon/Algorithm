n, m = map(int, input().split())
basket = [i for i in range(1, n+1)]
for i in range(m):
    left, right = map(int, input().split())
    basket[left-1:right] = basket[left-1:right][::-1]
print(*basket)