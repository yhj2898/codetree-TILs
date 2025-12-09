m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
def days(m,d):
    DOM=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    total_days=0

    for i in range(m):
        total_days += DOM[i]
    total_days +=d
    return total_days

day_diff = days(m2,d2) - days(m1,d1)
weekday=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
idx=0
for i in range(7):
    if weekday[i] == A:
        idx = i

print((days(m2,d2) - (days(m1,d1)+idx))//7 +1)