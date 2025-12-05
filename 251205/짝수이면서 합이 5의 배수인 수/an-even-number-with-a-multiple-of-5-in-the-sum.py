n = int(input())

# Please write your code here.
def is_true(n):
    return n%2==0 and (n//10 + n%10) %5==0

if is_true(n):
    print('Yes')
else:
    print('No')