vacation_pr = float(input())
puzzles_number = int(input())
dolls_number = int(input())
bear_number = int(input())
minions_number = int(input())
trucks_number = int(input())

total = puzzles_number * 2.60 + dolls_number * 3 + bear_number * 4.10 + minions_number * 8.20 + \
        trucks_number * 2
total_toys = puzzles_number + dolls_number + bear_number + minions_number + trucks_number

if total_toys > 50:
    total *= 0.75

rent = total * 0.10

profit = total - rent
diff = abs(profit - vacation_pr)

if profit >= vacation_pr:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
