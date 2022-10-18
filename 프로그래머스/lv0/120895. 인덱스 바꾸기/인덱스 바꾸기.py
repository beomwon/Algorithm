def solution(my_string, num1, num2):
    my_string = list(my_string)
    swap=my_string[num1]
    my_string[num1] = my_string[num2]
    my_string[num2] = swap
    
    return ''.join(my_string)