n = int(input())

class student:
    def __init__(self, name, a, b, c):
        self.name, self.a, self.b, self.c = name, a, b, c

students=[]
for _ in range(n):
    name, a, b, c = tuple(input().split())
    students.append(student(name,int(a),int(b),int(c)))

students.sort(key=lambda x: x.a + x.b + x.c)

for s in students:
    print(s.name, s.a, s.b, s.c)