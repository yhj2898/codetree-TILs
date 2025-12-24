x, y = map(int, input().split())

cnt=0
for i in range(x,y+1):
    if list(str(i)) == list(str(i))[::-1]:
        cnt+=1
print(cnt)