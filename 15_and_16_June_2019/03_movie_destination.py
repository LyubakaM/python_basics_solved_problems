from math import floor

budget = float(input())
destination = input()
season = input()
days_count = float(input())

price = 0

if destination == "Sofia":
    if season == "Winter":
        price += 17000
    elif season == "Summer":
        price += 12500
elif destination == "Dubai":
    if season == "Winter":
        price += 45000
    elif season == "Summer":
        price += 40000
elif destination == "London":
    if season == "Winter":
        price += 24000
    elif season == "Summer":
        price += 20250

total = 0

if destination == "Dubai":
    total = (price * days_count) * 0.70

elif destination == "Sofia":
    total = (price * days_count) * 1.25
elif destination == "London":
    total = price * days_count

diff = abs(budget - total)

if budget >= total:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")

