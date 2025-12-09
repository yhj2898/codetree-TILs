a, b = map(int, input().split())
n = list(map(int, input()))

# Please write your code here.
num=0

for i in n:
    num = num*a + n[i]

digits=[]
while True:
    if num<b:
        digits.append(num)
        break
    digits.append(num%b)
    num//=b

for i in digits[::-1]:
    print(i, end='')