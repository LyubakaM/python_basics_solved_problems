budget = float(input())
season = input()

destination = ""
accommodation = ""
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.30
        accommodation = "Camp"
    elif season == "winter":
        price = budget * 0.70
        accommodation = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.40
        accommodation = "Camp"
    elif season == "winter":
        price = budget * 0.80
        accommodation = "Hotel"
else:
    destination = "Europe"
    price = budget * 0.90
    accommodation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{accommodation} - {price:.2f}")
