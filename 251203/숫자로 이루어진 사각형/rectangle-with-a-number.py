n = int(input())

# Please write your code here.
def rec(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    cnt=1
    
    for i in arr:
        for j in range(n):
            i[j]=cnt
            cnt+=1
            if cnt==10:
                cnt=1
    
    for i in arr:
        for j in i:
            print(j, end=' ')
        print()
rec(n)