from itertools import permutations

length, num = map(int,input().split())
items = map(int, input().split())

for tuple_ in sorted(set(permutations(items, num))):
    print(' '.join(map(str,tuple_)))