kozunaks_count = int(input())
eggs_box_count = int(input())
cookies_kgs = int(input())

kozunaks_price = kozunaks_count * 3.20
eggs_price = eggs_box_count * 4.35
cookies_price = cookies_kgs * 5.40
eggs_paint_price = eggs_box_count * 12 * 0.15
total = kozunaks_price + eggs_price + cookies_price +eggs_paint_price
print(f"{total:.2f}")