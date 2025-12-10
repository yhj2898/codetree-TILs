N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
answer = [0 for _ in range(N+1)]
found = False

for s in student:
    answer[s]+=1
    if answer[s]>=K:
        print(s)
        found = True
        break
if found == False:
    print(-1)