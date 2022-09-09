res = 0
for _ in range(int(input())):
    word = input()
    check = word[0]
    store = [check]
    flag = True
    for i in range(1,len(word)):
        if word[i] != check and word[i] not in store:
            store.append(word[i])
            check = word[i]
        elif word[i] == word[i-1]:
            pass
        else:
            flag = False
            break
    if flag:
        res += 1

print(res)