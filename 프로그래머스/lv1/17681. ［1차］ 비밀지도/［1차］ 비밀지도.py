def solution(n, a, b):
    answer = []
    for x, y in zip(a, b):
        answer.append(str(bin(x|y))[2:].rjust(n,' ').replace('0',' ').replace('1','#'))
    return answer
        
    
# def solution(n, arr1, arr2):
#     answer = []
#     for x,y in zip(arr1,arr2):
#         temp = [0]*n
#         length = len(format(bin(x|y))[2:])
#         temp[n-length:] = map(int,format(bin(x|y))[2:])
        
#         wall_check = ''
#         for wall in temp:
#             if wall: wall_check += '#'
#             else: wall_check += ' '
            
#         answer.append(wall_check)
        
#     return answer