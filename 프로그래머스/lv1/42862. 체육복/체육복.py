def solution(n, lost, reserve):
    student = [1 for _ in range(n)]
    for l in lost:
        student[l-1] -= 1
    for r in reserve:
        student[r-1] += 1
    student = [1] + student + [1]
    
    for i in range(1, n+1):
        if student[i] == 2:
            if student[i-1] == 0:
                student[i-1] = 1
                student[i] = 1
            elif student[i+1] == 0:
                student[i+1] = 1
                student[i] = 1
    return n - student.count(0)