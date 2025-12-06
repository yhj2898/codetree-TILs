text = input()
pattern = input()

# Please write your code here.
def find():
    if pattern in text:
        return text.index(pattern)
    else:
        return -1

print(find())