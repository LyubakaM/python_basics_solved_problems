from math import pi
r = float(input())

area = round(r * r * pi, 2)
cir = round((pi * r) * 2, 2)

print(f"{area:.2f}")
print(f"{cir:.2f}")
