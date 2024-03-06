def solution(bandage, health, attacks):
    casting_second, current_health, end = 0, health, attacks[-1][0]+1
    casting_success, heal, additional_heal = bandage
    
    for time in range(end):
        if time == attacks[0][0]: # 현재시간에 공격이 들어오면
            _, damage = attacks.pop(0)
            current_health -= damage
            casting_second = 0
            if current_health <= 0:
                return -1
        else: # 공격이 들어오지 않으면
            casting_second += 1
            if casting_second == casting_success:
                casting_second = 0
                current_health += additional_heal
            current_health += heal
            current_health = min(health, current_health)
            
    return current_health