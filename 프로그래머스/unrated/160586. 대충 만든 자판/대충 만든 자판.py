def solution(keymap, targets):
    answer = []
    kv = {}
    for keys in keymap:
        for index, key in enumerate(keys):
            if key in kv.keys():
                kv[key] = min(index+1, kv[key])
            else:
                kv[key] = index+1
                
    for target in targets:
        try:
            answer.append(sum([kv[key] for key in target]))
        except:
            answer.append(-1)
    return answer