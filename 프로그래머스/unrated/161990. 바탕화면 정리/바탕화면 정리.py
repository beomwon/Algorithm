def solution(wallpaper):
    answer = [50, 50, 0, 0]
    for yi, y in enumerate(wallpaper):
        for xi, x in enumerate(y):
            if x == '#':
                answer = [
                            min(answer[0], yi), min(answer[1], xi),
                            max(answer[2], (yi+1)), max(answer[3], (xi+1))
                         ]
    return answer