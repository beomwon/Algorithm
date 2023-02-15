def solution(quiz):
    return ['X' if eval(v.split('=')[0]) != int(v.split('=')[1]) else 'O' for v in quiz ]