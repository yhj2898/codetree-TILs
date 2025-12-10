N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.
handshakes.sort(key=lambda x: x[0])
inf = [0 for _ in range(N+1)]
inf[P] = 1
cnt=0
for t, x, y in handshakes:
    if x==P:
        inf[y] = 1
        cnt+=1
    elif y==P:
        inf[x] =1
        cnt+=1
    if cnt>=2:
        break

for i in range(1,N+1):
    print(inf[i], end='')