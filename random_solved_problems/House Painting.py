x = float(input())
y = float(input())
h = float(input())

walls1 = x * y
wind = 1.5 * 1.5
all_walls = 2 * walls1 - 2 * wind
back_wall = x * x
ent = 1.2 * 2
all_back = 2 * back_wall - ent
total_area = (all_back + all_walls)
green_paint = (total_area / 3.4)

roof_sq = 2 * (x * y)
roof_triangle1 = x * h / 2
roof_triangle2 = roof_triangle1 * 2
roof_area = roof_sq + roof_triangle2
red_paint = roof_area / 4.3
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
