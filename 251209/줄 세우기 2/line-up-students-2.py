n = int(input())

class Student:
    def __init__(self, h, w, no):
        self.h, self.w, self.no = h, w, no

students=[]
for i in range(n):
    h, w = map(int, input().split())
    no = i+1
    students.append(Student(h,w,no))

students.sort(key=lambda x: (x.h, -x.w))

for s in students:
    print(s.h, s.w, s.no)