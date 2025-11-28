a1, a2 = input().split()
b1, b2 = input().split()
c1, c2 = input().split()

a2 = int(a2)
b2 = int(b2)
c2 = int(c2)

if ((a1=='Y'and a2>=37) and (b1=='Y'and b2>=37)) or ((a1=='Y'and a2>=37) and (c1=='Y'and c2>=37)) or ((b1=='Y'and b2>=37) and (c1=='Y'and c2>=37)):
    print('E')
else:
    print('N')