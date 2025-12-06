n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def sum_f(queries):
    global arr
    for a,b in queries:
        total=0
        for i in range(a,b+1):
            total += arr[i-1]
        print(total)

sum_f(queries)