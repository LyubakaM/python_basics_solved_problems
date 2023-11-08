stadium_capacity = int(input())
fans_number = int(input())
a_count = 0
b_count = 0
v_count = 0
g_count = 0
stadium_count = 0

for _ in range(1, fans_number + 1):
    fan_sector = input()
    if fan_sector == "A":
        a_count += 1
    elif fan_sector == "B":
        b_count += 1
    elif fan_sector == "V":
        v_count += 1
    elif fan_sector == "G":
        g_count += 1
fans_a = (a_count / fans_number) * 100
fans_b = (b_count / fans_number) * 100
fans_v = (v_count / fans_number) * 100
fans_g = (g_count / fans_number) * 100
capacity_all = (fans_number / stadium_capacity) * 100
print(f"{fans_a:.2f}%")
print(f"{fans_b:.2f}%")
print(f"{fans_v:.2f}%")
print(f"{fans_g:.2f}%")
print(f"{capacity_all:.2f}%")
