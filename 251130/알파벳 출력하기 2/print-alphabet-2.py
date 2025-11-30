n=int(input())

x=ord('A')

for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for j in range(n-i):
        print(chr(x), end=' ')
        x+=1
        if x>ord('Z'):
            x=ord('A')
    print()