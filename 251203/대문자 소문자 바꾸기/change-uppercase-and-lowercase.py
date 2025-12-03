x = input()
answer=''
for i in x:
    if i == i.lower():
        answer += i.upper()
    elif i== i.upper():
        answer += i.lower()
print(answer)