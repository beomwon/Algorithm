for _ in range(int(input())):
    length, target = map(int,input().split())
    q = [[v,i] for i,v in enumerate(list(map(int,input().split())))]
    sort_q = sorted(q, reverse=True)
    count=0
    while True:
        if q[0][0] == sort_q[0][0]:
            count+=1
            if target == q[0][1]:
                break
            q.pop(0)
            sort_q.pop(0)
        else:
            q.append(q.pop(0))
    print(count)