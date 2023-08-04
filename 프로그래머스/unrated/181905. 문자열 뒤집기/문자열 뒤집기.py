def solution(s, l, r):
    return s[:l] + s[l:r+1][::-1] + s[r+1:]