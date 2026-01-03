n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

xs = []
for xi in x:
    if xi not in xs:
        xs.append(xi)
def dfs(idx, cnt, chosen_x):
    if cnt > 3:
        return False

    remain_y = set()
    for i in range(n):
        if x[i] not in chosen_x:
            remain_y.add(y[i])

    if len(remain_y) <= 3 - cnt:
        return True

    if idx == len(xs):
        return False

    chosen_x.append(xs[idx])
    if dfs(idx + 1, cnt + 1, chosen_x):
        return True
    chosen_x.pop()

    if dfs(idx + 1, cnt, chosen_x):
        return True

    return False
if dfs(0, 0, []):
    print(1)
else:
    print(0)
