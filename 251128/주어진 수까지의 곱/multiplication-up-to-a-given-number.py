a,b = map(int, input().split())

m = 1
for i in range(a,b+1):
    m *=i
print(m)