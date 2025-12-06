n = int(input())

# Please write your code here.
def p_star(n):
    if n==0:
        return
    print('* '*n)
    p_star(n-1)
    print('* '*n)

p_star(n)
    