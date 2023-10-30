contract_time = input()
contract_type = input()
net_yes_no = input()
months_to_pay = int(input())
price = 0
discount = 0
if contract_time == "one":
    if contract_type == "Small":
        price += 9.98
    elif contract_type == "Middle":
        price += 18.99
    elif contract_type == "Large":
        price += 25.98
    elif contract_type == "ExtraLarge":
        price += 35.99
elif contract_time == "two":
    discount = 0.9625
    if contract_type == "Small":
        price += 8.58
    elif contract_type == "Middle":
        price += 17.09
    elif contract_type == "Large":
        price += 23.59
    elif contract_type == "ExtraLarge":
        price += 31.79
if net_yes_no == "yes":
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85
if discount > 0:
    print(f"{(price * months_to_pay) * discount:.2f} lv.")
else:
    print(f"{price * months_to_pay:.2f} lv.")
