n = int(input())
if n == 1: print('2')
else:
    while(True):  
        check = True

        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                check = False
                break

        if check:
            temp = str(n)
            if temp == temp[::-1]:
                print(temp)
                break

        n += 1