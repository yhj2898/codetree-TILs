a, b = map(int, input().split())

# Please write your code here.
def is_three(n):
    return '3' in list(str(n)) or '6' in list(str(n)) or '9' in list(str(n))


def f(a,b):
    cnt=0
    for i in range(a,b+1):
        if is_three(i) or i%3==0:
            cnt+=1
    print(cnt)

f(a,b)
