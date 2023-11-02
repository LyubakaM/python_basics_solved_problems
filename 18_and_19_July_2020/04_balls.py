from math import floor

number = int(input())
points = 0
counter = 0
red_c = 0
orange_c = 0
yellow_c = 0
white_c = 0
black_c = 0
no_color = 0

for balls in range(number):
    color = input()
    if color == "red":
        points += 5
        red_c += 1
    elif color == "orange":
        points += 10
        orange_c += 1
    elif color == "yellow":
        points += 15
        yellow_c += 1
    elif color == "white":
        points += 20
        white_c += 1
    elif color == "black":
        points /= 2
        black_c += 1
    else:
        no_color += 1
        continue
tot = floor(points)
print(f"Total points: {round(tot)}")
print(f"Red balls: {red_c}")
print(f"Orange balls: {orange_c}")
print(f"Yellow balls: {yellow_c}")
print(f"White balls: {white_c}")
print(f"Other colors picked: {no_color}")
print(f"Divides from black balls: {black_c}")
