student = [str(i) for i in range(1, 31)]
for _ in range(28):
    student.remove(input())

print(student[0])
print(student[1])