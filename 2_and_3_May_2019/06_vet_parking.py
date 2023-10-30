days = int(input())
hours_per_day = int(input())
day_index = 0

for single_day in range(days):
    parking_money = 0

    for hour in range(hours_per_day):
        day_index += 1
        if single_day % 2 == 0 and hour % 2 != 0:
            parking_money += 2.50
        elif single_day % 2 != 0 and hour % 2 != 0:
            parking_money += 1.25
        else:
            parking_money += 1

    print(f"Day: {day_index} – {parking_money} leva")