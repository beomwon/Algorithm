def solution(my_string, alp):
    return my_string.lower().replace(alp, chr(ord(alp)-32))