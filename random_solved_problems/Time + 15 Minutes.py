hour = int(input())
minutes = int(input())

total_time_minutes = hour * 60 + minutes + 15
hours2 = total_time_minutes // 60
minutes2 = total_time_minutes % 60

if hours2 > 23:
    hours2 = 0

if minutes2 < 10:
    print(f"{hours2}:0{minutes2}")
else:
    print(f"{hours2}:{minutes2}")



