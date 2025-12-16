n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

answer = [0]*10001
for i in range(n):
    if c[i]=='G':
        answer[x[i]]=1
    else:
        answer[x[i]]=2
max_score = 0
for i in range(1,10000-k+1):
    score=0
    for j in range(i,i+k+1):
        score+=answer[j]
    max_score = max(max_score,score)
print(max_score)