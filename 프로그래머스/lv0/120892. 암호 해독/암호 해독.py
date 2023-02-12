def solution(cipher, code):
    return ''.join([w for i, w in enumerate(cipher) if (i+1)%code == 0])