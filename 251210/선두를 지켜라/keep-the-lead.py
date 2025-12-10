n, m = map(int, input().split())

offset = 1000000
a = [0]*(offset+1)
b = [0]*(offset+1)

time_a = 1
for _ in range(n):
    v, t = tuple(map(int, input().split()))
    for _ in range(t):
        a[time_a] = a[time_a-1] + v
        time_a +=1

time_b = 1
for _ in range(m):
    v,t = tuple(map(int, input().split()))
    for _ in range(t):
        b[time_b] = b[time_b-1] + v
        time_b +=1

leader, ans = 0, 0
for i in range(1, time_a):
    if a[i]>b[i]:
        if leader == 'b':
            ans +=1
        leader = 'a'
    elif a[i]<b[i]:
        if leader == 'a':
            ans+=1
        leader = 'b'
print(ans)