unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class mission:
    def __init__(self,unlock_code, wire_color, seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds

mission1 = mission(unlock_code, wire_color,seconds)
print(f'code : {mission1.unlock_code}')
print(f'color : {mission1.wire_color}')
print(f'second : {mission1.seconds}')