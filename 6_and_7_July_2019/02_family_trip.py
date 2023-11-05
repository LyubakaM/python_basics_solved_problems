budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
aux_percent = int(input())

if number_of_nights > 7:
    price_per_night *= 0.95

total_night_price = price_per_night * number_of_nights
aux_price = budget * (aux_percent/100)
total_total = total_night_price + aux_price
diff = abs(budget - total_total)
if total_total <= budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")