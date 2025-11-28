a,b = map(int, input().split())

# 정수
print(f'{a//b}.',end='')

# 소수
for i in range(20):
    print(a%b * 10 //b, end='')