A = input()

# Please write your code here.
def f(a):
    for i in a:
        for j in a:
            if i!=j:
                return True
    return False

if f(A):
    print('Yes')
else:
    print('No')