n = int(input())

# Please write your code here.
def print_up(x):
    if x>n:
        return
    print(x, end=' ')
    print_up(x+1)

def print_down(x):
    if x<1:
        return
    print(x, end=' ')
    print_down(x-1)

print_up(1)
print()
print_down(n)