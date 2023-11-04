flour_price_kg = float(input())
flour_kgs = float(input())
sugar_kgs = float(input())
eggs_box_count= int(input())
yest_count = int(input())

sugar_price = flour_price_kg * 0.75
eggs_price = flour_price_kg * 1.1
yest_price = sugar_price * 0.2
flour_count = flour_price_kg * flour_kgs
sugar_count = sugar_price * sugar_kgs
eggs_count = eggs_price * eggs_box_count
yest_count = yest_price * yest_count
total = flour_count + sugar_count + eggs_count + yest_count

print(f"{total:.2f}")