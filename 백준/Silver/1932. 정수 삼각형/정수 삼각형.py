n = int(input())
triangle = [[0,int(input()),0]]
for i in range(1,n):
    triangle.append([0]+[int(x) + max(triangle[-1][i],triangle[-1][i+1]) for i, x in enumerate(input().split())]+[0])

print(max(triangle[-1]))