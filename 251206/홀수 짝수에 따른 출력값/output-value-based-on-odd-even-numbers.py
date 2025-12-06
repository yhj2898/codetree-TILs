N = int(input())

# Please write your code here.
def f(n):
    if n<=1:
        return n    
    return f(n-2) + n
print(f(N))