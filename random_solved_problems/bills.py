months = int(input())
electricity = 0
water = 0
internet = 0
others = 0

total_sum = 0

for curr_turn in range(months):
    curr_bill = float(input())
    electricity += curr_bill
    water += 20
    internet += 15
    others += (curr_bill + 20 + 15) * 1.20

average = (electricity + water + internet + others) / months
print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {average:.2f} lv")