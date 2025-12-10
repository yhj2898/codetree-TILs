n, m = map(int, input().split())
first = [0]* 1000000

a=[0]* 1000000
b=[0]* 1000000

ta=1
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        a[ta] = a[ta-1] + v
        ta+=1
tb=1
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        b[tb] = b[tb-1] + v
        tb+=1
leader=''
cnt=0
for i in range(ta):
    if a[i]>b[i]:
        if leader=='b' or leader =='ab':
            cnt+=1
        leader = 'a'
    if a[i]<b[i]:
        if leader =='a' or leader == 'ab':
            cnt+=1
        leader = 'b'
    if a[i]==b[i]:
        if leader == 'a' or leader=='b':
            cnt+=1
        leader = 'ab'
print(cnt)