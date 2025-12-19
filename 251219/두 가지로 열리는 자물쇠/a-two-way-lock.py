n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def dist(x,y):
    return min(abs(x-y),n-abs(x-y)) <=2
cnt=0
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            first = dist(a1,i) and dist(b1,j) and dist(c1,k)
            second = dist(a2,i) and dist(b2,j) and dist(c2,k)
            if first or second:
                cnt+=1
print(cnt)