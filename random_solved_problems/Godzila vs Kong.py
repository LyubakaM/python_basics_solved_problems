budget = float(input())
statists = int(input())
cloths_price_per_statist = float(input())

decors = budget * 0.10
clothes_total = statists * cloths_price_per_statist

if statists > 150:
    clothes_total *= 0.90

total_cost = decors + clothes_total
diff = abs(total_cost - budget)

if budget >= total_cost:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")

else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
