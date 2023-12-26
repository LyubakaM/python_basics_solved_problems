n_age = int(input())
washer_price = float(input())
toy_price = int(input())

money = 0
money_for_years = 10

for years in range(1, n_age + 1):
    if years % 2 == 0:
        money += money_for_years
        money -= 1
        money_for_years += 10
    else:
        money += toy_price
diff = abs(money - washer_price)
if money >= washer_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")