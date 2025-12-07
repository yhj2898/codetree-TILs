n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
words=[]
for i in str:
    if i[:len(t)] == t:
        words.append(i)

words.sort()

print(words[k-1])