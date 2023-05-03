def solution(my_string):
    l, u = [0]*26, [0]*26
    for char in my_string:
        if char.islower():
            l[ord(char)-ord('a')] += 1
        else:
            u[ord(char)-ord('A')] += 1
    return u+l