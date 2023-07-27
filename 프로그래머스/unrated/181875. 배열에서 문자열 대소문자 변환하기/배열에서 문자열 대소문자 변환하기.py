def solution(s):
    return [v.upper() if i%2 else v.lower() for i, v in enumerate(s)]