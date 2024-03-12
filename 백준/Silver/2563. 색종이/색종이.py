arr = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(int(input())):
    y, x = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[y+i][x+j] = 1
            
print(sum(sum(arr, [])))