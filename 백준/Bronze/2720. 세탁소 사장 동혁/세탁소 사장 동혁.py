for _ in range(int(input())):
    c = int(input())
    q, c = divmod(c, 25)
    d, c = divmod(c, 10)
    n, c = divmod(c, 5)
    print(q, d, n, c)