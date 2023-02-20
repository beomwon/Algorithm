def solution(food):
    answer = ['0']
    length = len(food)-1
    for i, v in enumerate(food[1:][::-1]):
        arrangement = [str(length-i) for _ in range(v//2)]
        answer =  arrangement + answer + arrangement
        
    return ''.join(answer)