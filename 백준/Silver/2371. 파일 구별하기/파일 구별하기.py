temp = []
max_ = 0
flag = True
for i in range(int(input())):
    temp.append([int(x) for x in input().split() if x != '-1'])
    if len(temp[-1]) > max_: max_ = len(temp[-1])

for i in range(len(temp)):
    if len(temp[i]) != max_:
        temp[i] += [0 for _ in range(max_-len(temp[i]))]

for i in range(len(temp[0])):
    digit = []
    for j in range(len(temp)):
        digit.append(temp[j][i])
    if len(digit) == len(set(digit)):
        print(i+1)
        flag = False
        break
if flag: print(max_)