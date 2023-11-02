budget = float(input())
serials_n = int(input())


for serial in range(serials_n):
    serial_name = input()
    price = float(input())
    if serial_name == "Thrones":
        price /= 2

    elif serial_name == "Lucifer":
        price *= 0.6

    elif serial_name == "Protector":
        price *= 0.7

    elif serial_name == "TotalDrama":
        price *= 0.8
    elif serial_name == "Area":
        price *= 0.9
    budget -= price
if budget >= 0:
    print(f"You bought all the series and left with {abs(budget):.2f} lv.")
else:
    print(f"You need {abs(budget):.2f} lv. more to buy the series!")
