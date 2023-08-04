def solution(id_list, report, k):
    report = set(report)
    t = [v.split()[1] for v in report]
    r = [v for v in id_list if k<=t.count(v)]
    answer = [0]*len(id_list)
    
    for v in report:
        a, b = v.split()
        answer[id_list.index(a)] += int(b in r)
    
    return answer
            
# def solution(id_list, report, k):
#     result = []
#     info = {key: {'report': [], 'count': 0} for key in id_list}
    
#     for history in set(report):
#         reporter, offender = history.split()
#         info[reporter]['report'].append(offender)
#         info[offender]['count'] += 1
    
#     for user in id_list:
#         count = 0
#         for offender in info[user]['report']:
#             if k <= info[offender]['count']:
#                 count += 1
        
#         result.append(count)
        
#     return result