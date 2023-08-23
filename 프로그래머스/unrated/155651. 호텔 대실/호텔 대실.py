# def time_convert(string) :
#     h, m = map(int, string.split(":"))
#     return h*60 + m

# def solution(book_time):
#     answer = 0
#     check_change_list = list()
#     for start, end in book_time :
#         check_change_list.append((time_convert(start), 1))
#         check_change_list.append((time_convert(end)+10, 0))

#     check_change_list.sort()

#     tmp = 0
#     for t, chk in check_change_list :
#         tmp += -1 if chk == 0 else 1
#         answer = max(answer, tmp)
#     return answer

def solution(book_time):
    timeline = [] 
    for s, e in book_time:
        sh, sm = map(int, s.split(':'))
        eh, em = map(int, e.split(':'))
        timeline += [(sh*60+sm, 1), (eh*60+em+10, 0)]
    
    answer, room = 0, 0
    for _, is_check_in in sorted(timeline):
        room += 1 if is_check_in else -1
        answer = max(answer, room)
    
    return answer
        