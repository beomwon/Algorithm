def solution(files):
    decom = []
    for index, file in enumerate(files):
        file = file.lower()
        decom.append([index,'',''])
        number_section = False
        for w in file:
            if w.isdigit():
                number_section = True
                decom[-1][2] += w
            else:
                if number_section:
                    break
                decom[-1][1] += w
        decom[-1][2] = int(decom[-1][2])
    
    decom = sorted(decom, key=lambda x: (x[1],x[2],x[0]))
    return [files[v[0]] for v in decom]