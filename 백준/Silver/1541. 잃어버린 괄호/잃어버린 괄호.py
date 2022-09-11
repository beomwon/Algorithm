formula = []
for arithmetic in input().split('-'):
    result = 0
    for v in arithmetic.split('+'):
        result += int(v)
    formula.append(result)

n = formula[0]
for i in range(1, len(formula)):
    n -= formula[i]
    
print(n)