s,q = input().split()
s = list(s)
q = int(q)

for _ in range(q):
    ques = input().split()

    if ques[0] == '1':
        a = int(ques[1]) -1
        b = int(ques[2]) -1
        s[a], s[b] = s[b], s[a]

    elif ques[0] == '2':
        x = ques[1]
        y = ques[2]
        for i in range(len(s)):
            if s[i]==x:
                s[i]=y
    print(''.join(s))
