a=input()
arr=['apple','banana','grape','blueberry','orange']

cnt=0
for s in arr:
    if s[2]==a or s[3]==a:
        print(s)
        cnt+=1
        
print(cnt)