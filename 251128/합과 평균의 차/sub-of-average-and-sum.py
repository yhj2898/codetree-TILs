a,b,c = map(int, input().split())
total = a+b+c
mean = total//3

print(total, mean, total-mean, sep='\n')