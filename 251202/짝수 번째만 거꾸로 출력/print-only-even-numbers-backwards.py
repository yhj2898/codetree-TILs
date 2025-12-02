a = input()
answer=''
for i in range(len(a)):
    if i%2==1:
        answer+=a[i]

print(answer[::-1])