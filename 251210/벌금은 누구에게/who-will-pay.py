N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
answer = [0 for _ in range(N+1)]

for s in student:
    answer[s]+=1
    if answer[s]>=3:
        print(s)
        break