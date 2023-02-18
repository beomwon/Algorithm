def solution(numer1, denom1, numer2, denom2):
    result = [numer1*denom2 + numer2*denom1, denom1*denom2]
    i=2
    while True:
        if i > min(result):
            break
            
        if result[0]%i == 0 and result[1]%i == 0:
            result[0]/=i
            result[1]/=i
        else:
            i+=1
    
    return result