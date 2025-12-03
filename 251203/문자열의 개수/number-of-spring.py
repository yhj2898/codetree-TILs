word = []

while True:
    x = input()
    if x == '0':
        break
    else:
        word.append(x)
print(len(word))

for i in range(len(word)):
    if i%2==0:
        print(word[i])