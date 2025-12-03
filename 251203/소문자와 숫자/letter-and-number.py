x = input()
answer=''
for i in x:
    if i.isalpha():
        answer += i.lower()
    elif i.isdigit():
        answer += i
print(answer)