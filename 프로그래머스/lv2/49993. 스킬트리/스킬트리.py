def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        _max = -1
        for step in skill_tree:
            if step in skill and skill.index(step) != (_max:=_max+1): break
        else:
            answer += 1
    
    return answer