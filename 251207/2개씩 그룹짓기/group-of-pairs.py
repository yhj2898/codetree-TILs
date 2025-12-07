n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()

x = []
for i in range(n):
    x.append(nums[i]+nums[2*n-i-1])

print(max(x))