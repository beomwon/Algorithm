def solution(park, routes):
    dog, width, height, block = {'y': 0, 'x': 0}, len(park[0]), len(park), []
            
    for y in range(len(park)):
        for x in range(len(park[0])):
            if park[y][x] == 'X': block.append([y, x])
            elif park[y][x] == 'S': dog = {'y': y, 'x': x}
            
    for route in routes:
        op, n = route.split()
        n = int(n)
        move = {'E': {'y': 0, 'x': n}, 'S': {'y': n, 'x': 0},'W': {'y': 0, 'x': -n}, 'N': {'y': -n, 'x': 0}}
        
        if 0 <= (dog['y'] + move[op]['y']) < height and 0 <= (dog['x'] + move[op]['x']) < width:
            check_block = True
            
            for y, x in block:
                if min(dog['y'], dog['y'] + move[op]['y']) <= y <= max(dog['y'], dog['y'] + move[op]['y']):
                    if min(dog['x'], dog['x'] + move[op]['x']) <= x <= max(dog['x'], dog['x'] + move[op]['x']):
                        check_block = False
                        break
                        
            if check_block:
                dog['y'] += move[op]['y']
                dog['x'] += move[op]['x']
        
    return [dog['y'],dog['x']]