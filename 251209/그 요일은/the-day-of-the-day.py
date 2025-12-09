m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
def days(m,d):
    DOM=[0,31,29,31,3,0,31,30,31,31,30,31,30,31]
    total_days=0

    for i in range(m):
        total_days += DOM[i]
    total_days +=d
    return total_days

day_diff = days(m2,d2) - days(m1,d1)
print(day_diff//7+1)