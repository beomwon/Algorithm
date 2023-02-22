def solution(str1, str2):
    answer = 0
    s1 = [str1[i].lower()+str1[i+1].lower() for i in range(len(str1)-1) if ('a'<=str1[i].lower()<='z' and 'a'<=str1[i+1].lower()<='z')]
    s2 = [str2[i].lower()+str2[i+1].lower() for i in range(len(str2)-1) if ('a'<=str2[i].lower()<='z' and 'a'<=str2[i+1].lower()<='z')]
    
    numerator = 0
    
    for v in s1:
        if v in s2:
            s2.remove(v)
            numerator+=1
    denominator = len(s1+s2)
    
    if numerator==0 and denominator==0:
        return 65536
    
    return int(numerator/denominator*65536)