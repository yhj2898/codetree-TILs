n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
ans=[]
for num in nums:
    if nums.count(num) ==1:
        ans.append(num)

if ans:
    print(max(ans))
else:
    print(-1)