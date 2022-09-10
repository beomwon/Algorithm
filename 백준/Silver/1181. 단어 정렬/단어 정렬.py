n = int(input())
lst = []

for i in range(n):
    lst.append(input())
set_lst = set(lst)	## set으로 변환해서 중복값을 제거
lst = list(set_lst)	## 다시 list로 변환
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)