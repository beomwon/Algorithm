def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        _max = -1
        iscorrect = True
        for step in skill_tree:
            if step in skill:
                if skill.index(step) == _max + 1:
                    _max += 1
                else:
                    iscorrect = False
                    break
                    
        if iscorrect: answer += 1
    
    return answer


# import re
# def solution(skill, skill_trees):
#     answer = 0
#     for s in skill_trees:
#         s = ''.join(re.findall(f'[{skill}]', s))
#         answer += int(s == skill[:len(s)])
#     return answer