def solution(myString, pat):
    return int(pat in myString.replace('A','C').replace('B','A').replace('C','B'))