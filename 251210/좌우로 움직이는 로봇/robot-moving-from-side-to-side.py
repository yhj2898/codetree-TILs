n, m = map(int, input().split())

offset = 1000000
a = [0] * (2*offset+1)
b = [0] * (2*offset+1)

time_a = 1
for _ in range(n):
    t, d = input().split()
    for _ in range(int(t)):
        a[time_a] = a[time_a -1] + (1 if d=='R' else -1)
        time_a+=1

time_b = 1
for _ in range(m):
    t, d = input().split()
    for _ in range(int(t)):
        b[time_b] = b[time_b -1] + (1 if d=='R' else -1)
        time_b +=1
if time_a<time_b:
    for i in range(time_a,time_b):
        a[i]=a[i-1]
elif time_a>time_b:
    for i in range(time_b,time_a):
        b[i]=b[i-1]

cnt=0
for i in range(1, max(time_a, time_b)):
    if a[i]==b[i] and a[i-1] != b[i-1]:
        cnt+=1
print(cnt)