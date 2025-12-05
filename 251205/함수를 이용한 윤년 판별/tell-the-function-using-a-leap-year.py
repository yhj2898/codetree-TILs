y = int(input())

# Please write your code here.
def leap_year(n):
    if n % 4 !=0:
        return False
    if n%100==0 and n%400 !=0:
        return False
    return True

if leap_year(y):
    print('true')
else:
    print('false')