def solution(genres, plays):
    answer = []
    site = {}
    for i, (genre, play) in enumerate(zip(genres,plays)):
        if genre in site.keys():
            site[genre] = [site[genre][0]+play, site[genre][1]+[[play,i]]]
        else:
            site[genre] = [play, [[play,i]]]
    for _, indexs in sorted(site.items(), key=lambda x: -x[1][0]):
        for index in sorted(indexs[1], key=lambda x: -x[0])[:2]:
            answer.append(index[1])
            
    return answer