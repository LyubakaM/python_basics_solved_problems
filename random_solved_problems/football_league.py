stadium_capacity = int(input())
fan_number = int(input())
a_count = 0
b_count = 0
v_count = 0
g_count = 0
home_count = 0
away_count = 0

for fan in range(fan_number):

    sector = input()

    if sector == "A":
        a_count += 1
    elif sector == "B":
        b_count += 1
    elif sector == "V":
        v_count += 1
    elif sector == "G":
        g_count += 1

ave_a = a_count / fan_number * 100
ave_b = b_count / fan_number * 100
ave_v = v_count / fan_number * 100
ave_g = g_count / fan_number * 100
all_fans_to_stadium = fan_number / stadium_capacity * 100

print(f"{ave_a:.2f}%")
print(f"{ave_b:.2f}%")
print(f"{ave_v:.2f}%")
print(f"{ave_g:.2f}%")
print(f"{all_fans_to_stadium:.2f}%")