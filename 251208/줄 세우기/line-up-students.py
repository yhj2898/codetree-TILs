n = int(input())

# Please write your code here.
class Student:
    def __init__(self, h, w, no):
        self.h, self.w, self.no = h, w, no

students=[]
for i in range(n):
    h, w = map(int,input().split())
    students.append(Student(h,w,i+1))

students.sort(key=lambda x: (-x.h, -x.w, x.no))

for i in students:
    print(i.h, i.w, i.no)