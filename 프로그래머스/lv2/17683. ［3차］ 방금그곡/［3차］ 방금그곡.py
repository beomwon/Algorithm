def solution(m, musicinfos):
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('A#','a').replace('G#','g')
    found = {'time': 0, 'name': '(None)'}
    
    for data in musicinfos:
        start, end, name, song = data.split(',')
        
        start_hour, start_min = map(int, start.split(':'))
        end_hour, end_min = map(int, end.split(':'))
        length = (end_hour-start_hour)*60 + (end_min-start_min)
        
        song = song.replace('C#','c').replace('D#','d').replace('F#','f').replace('A#','a').replace('G#','g')
        song = (song*max(1, int(length/len(song))+1))[:length]
        
        if m in song and found['time'] < length:
            found = {'time': length, 'name': name}
            
    return found['name']