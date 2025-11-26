nums = list(map(int,input().split()))

n = []
idx = []
for i in range(len(nums)):
    if nums[i] >250:
         idx.append(i)

n = nums[:min(idx)]

sum_val = 0
for i in n:
    sum_val += i

mean = round(sum_val / len(n),1)

print(sum_val, mean)