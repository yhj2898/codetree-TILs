a, b, c = map(int, input().split())

# Please write your code here.
if a*24*60 + b*60 + c > 11*24*60 + 11*60 + 11:
    print( (a-11)*60*24 + (b-11)*60 + c-11 )
else:
    print(-1)