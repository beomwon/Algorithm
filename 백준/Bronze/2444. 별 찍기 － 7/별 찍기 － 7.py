temp = int(input())
star = [i*2-1 for i in range(1, temp+1)]
star += star[:-1][::-1]

space = [*range(temp)]
space = space[::-1] + space[1:]

for st, sp in zip(star, space):
    print(' '*sp + '*'*st)