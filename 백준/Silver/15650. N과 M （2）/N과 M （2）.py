from itertools import combinations

length, num = map(int,input().split())
items = [x for x in range(1,length+1)]

for tuple_ in list(combinations(items, num)):
    print(' '.join(map(str,tuple_)))