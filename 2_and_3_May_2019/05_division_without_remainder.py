n = int(input())
p1 = 0
p1_num = 0
p2 = 0
p2_num = 0
p3 = 0
p3_num = 0

for nums in range(n):
    numbers_input = int(input())
    if numbers_input % 2 == 0:
        p1 += 1
    if numbers_input % 3 == 0:
        p2 += 1
    if numbers_input % 4 == 0:
        p3 += 1
p1_ave = (p1 / n) * 100
p2_ave = (p2 / n) * 100
p3_ave = (p3 / n) * 100

print(f"{p1_ave:.2f}%")
print(f"{p2_ave:.2f}%")
print(f"{p3_ave:.2f}%")
