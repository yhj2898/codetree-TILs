a, b, c = map(int, input().split())

# Please write your code here.
n = a*b*c
def multi(n):    
    if n<10:
        return n
    return multi(n//10) + n%10

print(multi(n))