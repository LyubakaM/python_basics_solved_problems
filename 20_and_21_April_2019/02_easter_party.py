guests_count = int(input())
kuvert_price = float(input())
desi_moneys = float(input())

price = 0

if 0 < guests_count < 10:
    price = kuvert_price
elif 10 <= guests_count <= 15:
    price = kuvert_price * 0.85
elif 15 < guests_count <= 20:
    price = kuvert_price * 0.80
else:
    price = kuvert_price * 0.75

cake_price = desi_moneys * 0.10
total = guests_count * price + cake_price
diff = abs(desi_moneys - total)

if desi_moneys >= total:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")





