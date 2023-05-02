def solution(my_string, indices):
    a = list(my_string)
    for v in indices:
        a[v] = ''
        
    return ''.join(a)