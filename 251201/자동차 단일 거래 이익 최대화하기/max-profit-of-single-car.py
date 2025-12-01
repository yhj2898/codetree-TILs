n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
m = min(price)
idx = price.index(min(price))

ans = price[idx:]
print(max(ans)-min(ans))
