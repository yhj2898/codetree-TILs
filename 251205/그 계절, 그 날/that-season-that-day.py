Y, M, D = map(int, input().split())

# Please write your code here.
def leap(y):
    if y % 4 != 0:
        return False
    if y%100 ==0 and y%400 !=0:
        return False
    return True

def last_day(y,m):
    if leap(y) and m==2:
        return 29
    else:
        if m in [1,3,5,7,8,10,12]:
            return 31
        elif m ==2:
            return 28
        elif m in [4,6,9,11]:
            return 30

if D <= last_day(Y,M):
    if M in [3,4,5]:
        print('Spring')
    elif M in [6,7,8]:
        print('Summer')
    elif M in [9,10,11]:
        print('Fall')
    else:
        print('Winter')
else:
    print(-1)