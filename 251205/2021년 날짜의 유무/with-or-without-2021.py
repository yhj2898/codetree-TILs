M, D = map(int, input().split())

# Please write your code here.
def cal(m,d):
    if m in [1,3,5,7,8,10,12]:
        if d<=31:
            return True
    elif m == 2:
        if d <=28:
            return True
    elif m in[4,6,9,11]:
        if d <30:
            return True

if cal(M,D):
    print('Yes')
else:
    print('No')