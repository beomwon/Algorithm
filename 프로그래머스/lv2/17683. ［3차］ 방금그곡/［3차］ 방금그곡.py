def solution(m, musicinfos):
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('A#','a').replace('G#','g')
    find = {'time': 0, 'name': '(None)'}
    
    for data in musicinfos:
        start, end, name, song = data.split(',')
        song = song.replace('C#','c').replace('D#','d').replace('F#','f').replace('A#','a').replace('G#','g')
        
        start_hour, start_min = map(int, start.split(':'))
        end_hour, end_min = map(int, end.split(':'))
        length = (end_hour-start_hour)*60 + (end_min-start_min)
        
        song = (song*max(1, int(length/len(song))+1))[:length]
        print(song)
        if m in song and find['time'] < length:
            find = {'time': length, 'name': name}
            
    return find['name']