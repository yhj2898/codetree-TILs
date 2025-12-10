n = int(input())

# Please write your code here.
answer = [0] * 2001
offset = 1000
start = offset

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'R':
        for i in range(start, start+x):
            answer[i] += 1
        start += x
    else:
        for i in range(start-x, start):
            answer[i] +=1
        start -= x

result = sum(1 for i in answer if i>=2)
print(result)