n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
# a, b, c = zip(*moves)
# a, b, c = list(a), list(b), list(c)

ans=0

for start in [1,2,3]:
    pos = start
    score = 0

    for i in range(n):
        a,b,c = moves[i]
        if pos==a:
            pos==b
        elif pos==b:
            pos==a
        if pos==c:
            score+=1
    ans = max(ans, score)