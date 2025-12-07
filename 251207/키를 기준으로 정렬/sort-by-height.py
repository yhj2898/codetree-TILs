n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
class info:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

infos = []
for i in range(n):
    infos.append(info(name[i], height[i], weight[i]))

infos.sort(key=lambda x: x.height)

for i in infos:
    print(i.name, i.height, i.weight)