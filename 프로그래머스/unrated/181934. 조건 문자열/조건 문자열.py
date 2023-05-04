def solution(ineq, eq, n, m):
    if ineq == '>':
        return int(n>m | (n==m if eq == '=' else False))
    return int(n<m | (n==m if eq =='=' else False))