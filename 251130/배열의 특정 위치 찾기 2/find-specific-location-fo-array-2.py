arr = list(map(int, input().split()))

odd=0
even=0

for i in range(len(arr)):
    if i%2==0:
        odd += arr[i]
    else:
        even += arr[i]

if odd>even:
    print(odd-even)
else:
    print(even-odd)