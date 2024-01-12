season = input()
km_per_month = float(input())
accommodation = ""
location = ""
price = 0

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price = 0.75
    elif season == "Summer":
        price = 0.90
    elif season == "Winter":
        price = 1.05
elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price = 0.95
    elif season == "Summer":
        price = 1.10
    elif season == "Winter":
        price = 1.25
elif 10000 < km_per_month <= 20000:
    price = 1.45

total = price * km_per_month
after_taxes = (total * 4) * 0.90

print(f"{after_taxes:.2f}")