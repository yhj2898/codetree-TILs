n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
answer=[]
cnt=1
for i in range(1,n):
    if arr[i]==arr[i-1]:
        cnt+=1
    else:
        answer.append(cnt)
        cnt=1
answer.append(cnt)
print(max(answer))

    

