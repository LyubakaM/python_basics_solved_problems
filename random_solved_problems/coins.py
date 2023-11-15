change = float(input())
change_counter = change * 1000
total = 0

while True:
    if change_counter >= 2000:
        change_counter -= 2000
    elif change_counter >= 1000:

        change_counter -= 1000
    elif change_counter >= 500:

        change_counter -= 500
    elif change_counter >= 200:

        change_counter -= 200
    elif change_counter >= 100:

        change_counter -= 100
    elif change_counter >= 50:

        change_counter -= 50
    elif change_counter >= 20:

        change_counter -= 20
    elif change_counter >= 10:

        change_counter -= 10
    total += 1
    if change_counter <= 0:
        break
print(total)

