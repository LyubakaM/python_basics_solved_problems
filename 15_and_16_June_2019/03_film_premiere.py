from math import floor

film_name = input()
type_of_treats = input()
ticket_count = int(input())
price = 0

if film_name == "John Wick":
    if type_of_treats == "Popcorn":
        price += 15
    elif type_of_treats == "Drink":
        price += 12
    elif type_of_treats == "Menu":
        price += 19
elif film_name == "Star Wars":
    if type_of_treats == "Popcorn":
        price += 25
    elif type_of_treats == "Drink":
        price += 18
    elif type_of_treats == "Menu":
        price += 30
elif film_name == "Jumanji":
    if type_of_treats == "Popcorn":
        price += 11
    elif type_of_treats == "Drink":
        price += 9
    elif type_of_treats == "Menu":
        price += 14

if film_name == "Jumanji" and ticket_count == 2:
    price *= 0.85
elif film_name == "Star Wars" and ticket_count >= 4:
    price *= 0.70

total = price * ticket_count
print(f"Your bill is {total:.2f} leva.")