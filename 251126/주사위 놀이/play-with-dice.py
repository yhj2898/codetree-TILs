result = list(map(int, input().split()))

cnt_arr = [0]*7

for i in result:
    cnt_arr[i] += 1

for i in range(1,7):
    cnt = cnt_arr[i]
    print(f'{i} - {cnt}')