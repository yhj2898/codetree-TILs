n=int(input())

x=ord('A')
for i in range(n):
    for j in range(i+1):
        print(chr(x), end='')
        x+=1
        if x==91:
            x=ord('A')
    
    print()