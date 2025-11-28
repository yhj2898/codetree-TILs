nums = list(map(int,input().split()))
n = []

for num in nums:
    if num <250:
        n.append(num)
    else:
        break

sum_val = 0
for i in n:
    sum_val += i

mean = round(sum_val / len(n), 1)
print(sum_val, mean)
