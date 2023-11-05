targeted_profit = float(input())
cocktails_profit = 0

while cocktails_profit < targeted_profit:
    command = input()
    if command == "Party!":
        diff = abs(targeted_profit - cocktails_profit)
        print(f"We need {diff:.2f} leva more.")
        break

    cocktails_number = int(input())
    len_nn = int(len(command))

    current_cocktail_price = len_nn * cocktails_number
    if current_cocktail_price % 2 == 1:
        current_cocktail_price *= 0.75

    cocktails_profit += current_cocktail_price

else:
    print("Target acquired.")

print(f"Club income - {cocktails_profit:.2f} leva.")