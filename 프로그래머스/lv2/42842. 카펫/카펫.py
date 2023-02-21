def solution(b, y):
    # b+y = w*h
    # (w-2)*(h-2) = y
    
    for i in range(3, b+y):
        if (b+y)%i==0 and ((i-2)*((b+y)/i -2)) == y:
            return sorted([i, (b+y)/i], reverse=True)