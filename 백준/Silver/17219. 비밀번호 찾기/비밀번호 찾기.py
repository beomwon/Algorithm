n, m = map(int, input().split())
dic = {}
for _ in range(n):
    key, value = input().split()
    dic[key] = value
   
for _ in range(m):
    print(dic[input()])
    