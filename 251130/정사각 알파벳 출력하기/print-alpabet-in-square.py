n=int(input())

x = ord('A')

for i in range(n):
    for j in range(n):
        print(chr(x), end='')
        x+=1
    print()