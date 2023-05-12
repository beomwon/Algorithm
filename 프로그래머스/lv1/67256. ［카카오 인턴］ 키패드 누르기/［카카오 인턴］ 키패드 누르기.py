def solution(numbers, hand):
    left = [0,0]
    right = [2,0]
    answer = ''
    keypad = [['*','7','4','1'],['0','8','5','2'],['#','9','6','3']]
    
    for temp in numbers:
        for x in range(3):
            for y in range(4):
                if keypad[x][y] == str(temp):
                    if x == 0:
                        left = [x,y]
                        answer += 'L'
                    elif x == 1:
                        left_dis = abs(left[0]-x) + abs(left[1]-y)
                        right_dis = abs(right[0]-x) + abs(right[1]-y)
                        if left_dis > right_dis:
                            right = [x,y]
                            answer += 'R'
                        elif left_dis < right_dis:
                            left = [x,y]
                            answer += 'L'
                        else:
                            if hand == 'left':
                                left = [x,y]
                                answer += 'L'
                            else:
                                right = [x,y]
                                answer += 'R'
                    else:
                        right = [x,y]
                        answer += 'R'
    return answer