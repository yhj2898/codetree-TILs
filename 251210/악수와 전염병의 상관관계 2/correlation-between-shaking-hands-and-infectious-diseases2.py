class Shake:
    def __init__(self, t, p1, p2):
        self.t, self.p1, self.p2 = t, p1, p2

n, k, p, t = map(int, input().split())
shakes=[]
for _ in range(t):
    t, p1, p2 = map(int, input().split())
    shakes.append(Shake(t, p1, p2))

shake_num=[0] * (n+1)
infected = [False] * (n+1)
infected[p] = True

shakes.sort(key=lambda x: x.t)

for s in shakes:
    target1 = s.p1
    target2 = s.p2

    if infected[target1]:
        shake_num[target1]+=1
    if infected[target2]:
        shake_num[target2]+=1

    if shake_num[target1]<=k and infected[target1]:
        infected[target2] = True
    if shake_num[target2]<=k and infected[target2]:
        infected[target1] = True

for i in range(1, n+1):
    if infected[i]:
        print(1, end='')
    else:
        print(0, end='')