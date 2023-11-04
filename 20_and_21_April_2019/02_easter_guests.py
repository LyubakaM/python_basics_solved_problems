from math import ceil

guests_count = int(input())
budget = int(input())

kozunaci_for_guest_count = ceil(guests_count / 3)
eggs_guest_count = guests_count * 2
kozunak_price = 4 * kozunaci_for_guest_count
eggs_price = eggs_guest_count * 0.45
total = kozunak_price + eggs_price
diff = abs(budget - total)
if budget >= total:
    print(f"Lyubo bought {kozunaci_for_guest_count} Easter bread and {eggs_guest_count} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")
