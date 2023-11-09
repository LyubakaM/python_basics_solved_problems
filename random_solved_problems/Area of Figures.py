import math
from math import pi

x = input()
area = 0

if x == "square":
    y = float(input())
    area = y * y

elif x == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b


elif x == "circle":
    r = float(input())
    area = (r*r) * math.pi


elif x == "triangle":
    h = float(input())
    lh = float(input())
    area = (h * lh) / 2

print(f"{area:.3f}")
