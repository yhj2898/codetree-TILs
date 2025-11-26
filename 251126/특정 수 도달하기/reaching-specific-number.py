nums = list(map(int,input().split()))

nums_sum=0
nums_avg=0

for n in nums:
    while n <= 250:
        nums_sum = sum(nums)
        nums_avg = sum(nums)/len(nums)
        break
    nums.pop()
    nums_sum = sum(nums)
    nums_avg = sum(nums)/len(nums)

print(nums_sum, nums_avg)