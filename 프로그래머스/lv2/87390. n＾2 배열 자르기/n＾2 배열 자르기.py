# solution=lambda n,l,r:[int(i%n)+1 if int(i/n) < int(i%n) else int(i/n)+1 for i in range(l,r+1)]

solution=lambda n,l,r:[i%n+1 if i//n < i%n else i//n+1 for i in range(l,r+1)]  

# def solution(n, left, right):
#     nums = [str(v) for v in range(1,n+1)]
#     flatten = [str(v)*(v-1) + ''.join(nums[(v-1):]) for v in range(1, n+1)]
#     return list(map(int,''.join(flatten)))[left:right+1]