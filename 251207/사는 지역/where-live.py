n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class p:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region

people=[]
for i in range(n):
    people.append(p(name[i],street_address[i],region[i]))

for i in people:
    if i.name == max(name):
        print(f'name {i.name}')
        print(f'addr {i.address}')
        print(f'city {i.region}')