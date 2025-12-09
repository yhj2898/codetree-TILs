n = int(input())

class Student:
    def __init__(self, name, h, w):
        self.name, self.h, self.w = name, h, w

students=[]
for _ in range(n):
    name, h, w = input().split()
    students.append(Student(name, int(h), int(w)))

students.sort(key = lambda x: (x.h, -x.w))

for s in students:
    print(s.name, s.h, s.w)