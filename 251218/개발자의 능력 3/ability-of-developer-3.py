x = list(map(int, input().split()))

def diff(a,b,c):
    sum1 = x[a] + x[b] + x[c]
    sum2 = sum(x) - sum1
    return abs(sum1-sum2)

min_diff=999

for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            min_diff = min(min_diff, diff(i,j,k))
print(min_diff)