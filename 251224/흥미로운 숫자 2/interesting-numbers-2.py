x, y = map(int, input().split())

def interesting(n):
    num = tuple(map(int, list(str(n))))
    for i in num:
        if num.count(i)==len(num)-1:
            return True
        
cnt=0
for i in range(x,y+1):
    if interesting(i):
        cnt+=1
print(cnt)
