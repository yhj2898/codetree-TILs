n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class forecast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

f=[]
for i in range(n):
    f.append(forecast(date[i], day[i], weather[i]))

rain=[]
for i in f:
    if i.weather == 'Rain':
        rain.append(i)

min_rain = rain[0]
for i in rain:
    if i.date < min_rain.date:
        min_rain = i

print(min_rain.date, min_rain.day, min_rain.weather)