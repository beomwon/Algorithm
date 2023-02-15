def solution(keyinput, board):
    x, y = board
    x = int(x/2)
    y = int(y/2)
    
    user_x, user_y = 0, 0
    for key in keyinput:
        if key == 'up': user_y += 1
        if key == 'down': user_y -= 1
        if key == 'left': user_x -= 1
        if key == 'right': user_x += 1
        
        user_y = min(user_y, y)
        user_y = max(user_y, -y)
        user_x = min(user_x, x)
        user_x = max(user_x, -x)
            
    return [user_x, user_y]