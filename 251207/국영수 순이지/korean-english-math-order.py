n=int(input())

class Student:
    def __init__(self, name, k, e, m):
        self.name, self.k, self.e, self.m = name, k, e, m

students=[]
for _ in range(n):
    name, k, e, m = tuple(input().split())
    students.append(Student(name,int(k),int(e),int(m)))

students.sort(key = lambda x: (-x.k,-x.e,-x.m))

for s in students:
    print(s.name, s.k, s.e, s.m)