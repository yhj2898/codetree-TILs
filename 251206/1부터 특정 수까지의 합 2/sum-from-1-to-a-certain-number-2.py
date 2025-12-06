N = int(input())

# Please write your code here.
def total(n):
    if n==1:
        return 1
    return total(n-1) + n

print(total(N))