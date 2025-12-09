n = 5

class Student:
    def __init__(self, name, h, w):
        self.name, self.h, self.w = name, h, w
    
students = []
for _ in range(5):
    name, h, w = input().split()
    students.append(Student(name, int(h), float(w)))

students.sort(lambda x: x.name)
print('name')
for i in students:
    print(i.name, i.h, f'{i.w:.1f}')
print()
students.sort(lambda x: -x.h)
print('height')
for i in students:
    print(i.name, i.h, f'{i.w:.1f}')