_ = input()
print(sum([(ord(x)-ord('a')+1)*(31**i) for i,x in enumerate(list(input()))])%1234567891)