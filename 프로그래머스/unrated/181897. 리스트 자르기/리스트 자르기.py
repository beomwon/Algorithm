def solution(n, slicer, num_list):
    a,b,c = slicer
    if n==1: a = 0; c = 1
    elif n==2: b = len(num_list)-1; c = 1
    elif n==3: c = 1
    return num_list[a:b+1:c]