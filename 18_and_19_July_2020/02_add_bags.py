price_lug_above_20kg = float(input())
luggage_kg = float(input())
days_to_departure = int(input())
luggage_count = int(input())

price = 0

if luggage_kg < 10:
    price = price_lug_above_20kg * 0.2
elif 10 <= luggage_kg <= 20:
    price = price_lug_above_20kg * 0.5
elif luggage_kg > 20:
    price = price_lug_above_20kg
if days_to_departure > 30:
    price += (price * 0.10)
elif 7 <= days_to_departure <= 30:
    price += (price * 0.15)
elif days_to_departure < 7:
    price += (price * 0.40)

total = price * luggage_count

print(f"The total price of bags is: {total:.2f} lv.")