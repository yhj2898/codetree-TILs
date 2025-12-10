n, m = map(int, input().split())

offset = 1000000
a = [0] * (2*offset+1)
b = [0] * (2*offset+1)

time_a = 1
for _ in range(n):
    t, d = input().split()
    for _ in range(int(t)):
        if d=='R':
            a[time_a] = a[time_a-1] +1
            time_a+=1
        else:
            a[time_a] = a[time_a-1] -1
            time_a+=1
time_b = 1
for _ in range(m):
    t, d = input().split()
    for _ in range(int(t)):
        if d=='R':
            b[time_b] = b[time_b-1] +1
            time_b+=1
        else:
            b[time_b] = b[time_b-1] -1
            time_b+=1

ans=0
for i in range(len(a)):
    if a[i]==b[i] and a[i-1]!=b[i-1]:
        ans+=1
print(ans)


