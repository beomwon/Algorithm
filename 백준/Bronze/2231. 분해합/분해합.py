target = int(input())
dic = {}
for i in range(1, 1000001):
    temp = i + sum(list(map(int,list(str(i)))))
    if temp in dic.keys():
        dic[temp].append(i)
    else:
        dic[temp] = [i]

    if target == temp:
        print(min(dic[temp]))
        break

if i == 1000000:
    print(0)