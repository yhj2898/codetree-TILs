product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class item:
    def __init__(self, name='', code=''):
        self.name = name
        self.code = code

item1 = item('codetree',50)
item2 = item(product_name, product_code)

print(f'product {item1.code} is {item1.name}')
print(f'product {item2.code} is {item2.name}')