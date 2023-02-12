def solution(s):
    stack = []
    for v in s.split():
        if v == 'Z':
            stack.pop()
        else:
            stack.append(int(v))
    return sum(stack)