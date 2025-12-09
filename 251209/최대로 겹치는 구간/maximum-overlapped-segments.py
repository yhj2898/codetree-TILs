n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer=[0] * 201
for a,b in segments:
    a += 100
    b += 100

    for i in range(a,b):
        answer[i] +=1

print(max(answer))