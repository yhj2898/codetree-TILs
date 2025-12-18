n, k = map(int, input().split())
offset = 100
candy = [0]*(2*offset+1)

# 바구니 좌표마다 사탕갯수 입력된 배열 만들기
for _ in range(n):
    cnt, b = map(int, input().split())
    candy[b+offset]+=cnt

max_cnt=0
for c in range(2*offset+1):
    total=0
    left = max(0,c-k)
    right = min(2*offset, c+k) 
    
    for i in range(left, right+1):
        total += candy[i]
    max_cnt = max(max_cnt, total)
print(max_cnt)