drink_type = input()
sugar_with_normal_extra = input()
drinks_number = int(input())
price = 0
discount = 0

if drink_type == "Espresso":
    if sugar_with_normal_extra == "Without":
        price += 0.90
    elif sugar_with_normal_extra == "Normal":
        price += 1
    elif sugar_with_normal_extra == "Extra":
        price += 1.20
elif drink_type == "Cappuccino":
    if sugar_with_normal_extra == "Without":
        price += 1
    elif sugar_with_normal_extra == "Normal":
        price += 1.20
    elif sugar_with_normal_extra == "Extra":
        price += 1.60
elif drink_type == "Tea":
    if sugar_with_normal_extra == "Without":
        price += 0.50
    elif sugar_with_normal_extra == "Normal":
        price += 0.60
    elif sugar_with_normal_extra == "Extra":
        price += 0.70
if sugar_with_normal_extra == "Without":
    price *= 0.65
if drink_type == "Espresso" and drinks_number >= 5:
    price *= 0.75
total = price * drinks_number
if total > 15:
    total *= 0.80
print(f"You bought {drinks_number} cups of {drink_type} for {total:.2f} lv.")


