n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for numbers in range(n):
    input_number = int(input())
    if input_number < 200:
        p1 += 1
    elif 200 <= input_number <= 399:
        p2 += 1
    elif 400 <= input_number <= 599:
        p3 += 1
    elif 600 <= input_number <= 799:
        p4 += 1
    else:
        p5 += 1
p1_r = (p1 / n) * 100
p2_r = (p2 / n) * 100
p3_r = (p3 / n) * 100
p4_r = (p4 / n) * 100
p5_r = (p5 / n) * 100

print(f"{p1_r:.2f}%")
print(f"{p2_r:.2f}%")
print(f"{p3_r:.2f}%")
print(f"{p4_r:.2f}%")
print(f"{p5_r:.2f}%")
