y, x, max_value = 1, 1, 0

for m in range(1, 10):
    lines = list(map(int, input().split()))
    if max_value < max(lines):
        max_value = max(lines)
        y, x = m, lines.index(max_value) + 1

print(max_value)
print(y, x)