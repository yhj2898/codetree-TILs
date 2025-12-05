n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def partial(a,b):
    for i in range(max(n1,n2) - min(n1,n2) +1):
        if a[i:i+min(n1,n2)] == b:
            return True
    return False 

if partial(a,b):
    print('Yes')
else:
    print('No')