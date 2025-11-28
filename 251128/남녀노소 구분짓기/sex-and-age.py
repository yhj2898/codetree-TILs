sex, age = [int(input()) for _ in range(2)]

if sex==0:
    if age>=19:
        print('MAN')
    else:
        print('BOY')
else:
    if age>=19:
        print('WOMAN')
    else:
        print('GIRL')