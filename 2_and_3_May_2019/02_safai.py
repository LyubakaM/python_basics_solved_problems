budget = float(input())
fuel = float(input())
day_of_week = input()

fuel_price = fuel * 2.10
total_plus_gid = fuel_price + 100

if day_of_week == "Sunday":
    total_plus_gid *= 0.80
elif day_of_week == "Saturday":
    total_plus_gid *= 0.90
res = abs(budget - total_plus_gid)
if budget >= total_plus_gid:
    print(f"Safari time! Money left: {budget-total_plus_gid:.2f} lv.")
elif budget < total_plus_gid:
    print(f"Not enough money! Money needed: {res:.2f} lv.")
