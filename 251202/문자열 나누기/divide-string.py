n=int(input())
arr = ''.join(input().split())

answer=''
for i in arr:
    answer += i
    if len(answer)==5:
        print(answer)
        answer=''
print(answer)