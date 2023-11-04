size = input()
color = input()
units_count = int(input())
sub_total = 0
if size == "Large":
    if color == "Red":
       sub_total += 16
    elif color == "Green":
       sub_total += 12
    elif color == "Yellow":
       sub_total += 9

elif size == "Medium":
    if color == "Red":
        sub_total += 13
    elif color == "Green":
        sub_total += 9
    elif color == "Yellow":
        sub_total += 7
elif size == "Small":
    if color == "Red":
       sub_total += 9
    elif color == "Green":
       sub_total += 8
    elif color == "Yellow":
       sub_total += 5
total = units_count * sub_total
expenses = total * 0.35
sum1 = total - expenses

print(f"{sum1:.2f} leva.")