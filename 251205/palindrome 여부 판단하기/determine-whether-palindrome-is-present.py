A = input()

# Please write your code here.
def palindrome(a):
    if a == a[::-1]:
        print('Yes')
    else:
        print('No')

palindrome(A)