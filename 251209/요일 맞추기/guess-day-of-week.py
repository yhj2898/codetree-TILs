m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.


def days(m,d):
    total_days=0
    DOM = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(m):
        total_days += DOM[i]
    
    total_days += d
    return total_days

day_diff = days(m2,d2) - days(m1,d1)

if day_diff % 7==0: 
    print('Mon')
elif day_diff % 7 ==1 or day_diff % 7 == -6:
    print('Tue')
elif day_diff % 7 ==2 or day_diff % 7 == -5:
    print('Wed')
elif day_diff % 7 ==3 or day_diff % 7 == -4:
    print('Thu')
elif day_diff % 7 ==4 or day_diff % 7 == -3:
    print('Fri')
elif day_diff % 7 ==5 or day_diff % 7 == -2:
    print('Sat')
else:
    print('Sun')