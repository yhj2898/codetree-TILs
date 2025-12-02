n=int(input())
arr = [input() for _ in range(n)]
s = input()

cnt=0
total=0
for i in arr:
    if i[0]==s:
        cnt+=1
        total+=len(i)

print(f'{cnt} {total/cnt:.2f}')