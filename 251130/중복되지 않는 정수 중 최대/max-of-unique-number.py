n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
max_val=0
for num in nums:
    if nums.count(num) ==1:
        if num>max_val:
            max_val = num
print(max_val)