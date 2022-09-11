for i in range(int(input())):
    temp = [1 if x =='(' else -1 for x in list(input())]
    before = temp[0]
    flag = True
    if before == -1: 
        print('NO')
        continue
    for v in temp[1:]:
        if before + v < 0:
            flag = False
            break
        else:
            before += v
    if flag and before == 0:
        print('YES')
    else:
        print('NO')