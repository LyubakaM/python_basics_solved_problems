budget = float(input())
br_video = int(input())
br_cpu = float(input())
br_ram = float(input())

video = br_video * 250
cpu = video * 0.35 * br_cpu
ram = video * 0.10 * br_ram
total = video + ram + cpu

if br_video > br_cpu:
    total = total * 0.85
else:
    total = total

diff = abs(budget - total)

if budget >= total:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")

