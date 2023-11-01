stage_of_tour = input()
ticket_type = input()
quantity = int(input())
picture_with_trophy = input() == "Y"

price = 0.0

if stage_of_tour == "Quarter final":
    if ticket_type == "Standard":
        price = 55.50
    elif ticket_type == "Premium":
        price = 105.20
    elif ticket_type == "VIP":
        price = 118.90
elif stage_of_tour == "Semi final":
    if ticket_type == "Standard":
        price = 75.88
    elif ticket_type == "Premium":
        price = 125.22
    elif ticket_type == "VIP":
        price = 300.40
elif stage_of_tour == "Final":
    if ticket_type == "Standard":
        price = 110.10
    elif ticket_type == "Premium":
        price = 160.66
    elif ticket_type == "VIP":
        price = 400.00

price *= quantity

if price > 4000:
    price *= 0.75
    picture_with_trophy = False
elif price > 2500:
    price *= 0.9

if picture_with_trophy:
    price += (quantity * 40)

print(f"{price:.2f}")