total = 0
cnt=0
while True:
    n=int(input())

    if 20<=n<30:
        total+=n
        cnt+=1
    else:
        break

print(f'{total/cnt:.2f}')