from math import floor, ceil


racket_price = float(input())
racket_count = int(input())
pairs_of_sneakers = int(input())
racket_tot = racket_count * racket_price
price_sneakers = racket_price / 6
price_sneakers_all = pairs_of_sneakers * price_sneakers
remaining_equipment = (racket_tot + price_sneakers_all) * 0.2
price_total = racket_tot + price_sneakers_all + remaining_equipment
price_jock = price_total / 8
price_sponsors = price_total * 7 / 8

print(f"Price to be paid by Djokovic {floor(price_jock)}")
print(f"Price to be paid by sponsors {ceil(price_sponsors)}")