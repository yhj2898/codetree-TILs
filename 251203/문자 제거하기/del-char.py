s=list(input())

while len(s)>1:
    n=int(input())
    if n<len(s):
        s.pop(n)
    else:
        s.pop()
    print(''.join(s))