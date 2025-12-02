s = input()
n=int(input())

if len(s)>n:
    print(s[:len(s)-n-1:-1])
else:
    print(s[::-1])