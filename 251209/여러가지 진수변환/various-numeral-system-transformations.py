N, B = map(int, input().split())

# Please write your code here.
answer = []
while True:
    if N < B:
        answer.append(N)
        break
    answer.append(N%B)
    N //= B

for i in answer[::-1]:
    print(i, end='')