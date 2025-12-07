secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class code:
    def __init__(self,code,place,time):
        self.code = code
        self.place = place
        self.time = time

a = code(secret_code, meeting_point, time)

print(f'secret code : {a.code}')
print(f'meeting point : {a.place}')
print(f'time : {a.time}')
