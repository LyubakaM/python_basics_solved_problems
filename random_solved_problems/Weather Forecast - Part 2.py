g = float(input())

if 26.00 <= g <= 35.00:
    print("Hot")
elif 20.1 <= g <= 25.9:
    print("Warm")
elif 15.00 <= g <= 20.00:
    print("Mild")
elif 12.00 <= g <= 14.9:
    print("Cool")
elif 5.00 <= g <= 11.9:
    print("Cold")
else:
    print("unknown")
