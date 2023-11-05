import math

high_wall = int(input())
width_wall = int(input())
no_paint_wall_percent = int(input())

paint_lt = input()
total_room_size = math.ceil((high_wall * width_wall * 4) * (1 - no_paint_wall_percent / 100))

while paint_lt != 'Tired!':
    paint_lt = int(paint_lt)

    total_room_size -= paint_lt

    if total_room_size < 0:
        print(f'All walls are painted and you have {abs(total_room_size)} l paint left!')
        break

    if total_room_size == 0:
        print('All walls are painted! Great job, Pesho!')
        break

    paint_lt = input()

else:
    print(f'{total_room_size} quadratic m left.')