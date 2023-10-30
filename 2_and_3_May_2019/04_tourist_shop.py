budget = float(input())
expenses_counter = 0
product = ""
day_counter = 0
end = False
items_count = 0
while budget >= 0:
    product = input()
    if product == "Stop":
        end = True
        break
    price = float(input())
    day_counter += 1
    if day_counter % 3 == 0:
        budget -= (price / 2)
        expenses_counter += (price / 2)
    else:
        budget -= price
        expenses_counter += price
    items_count += 1
diff = abs(budget)
if end:
    print(f"You bought {items_count} products for {expenses_counter:.2f} leva.")
else:
    print(f"You don't have enough money!")
    print(f"You need {diff:.2f} leva!")
