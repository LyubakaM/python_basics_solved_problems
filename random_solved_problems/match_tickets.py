budget = float(input())
category = input()
people_in_group = int(input())


ticket_price = 0

if 1 <= people_in_group <= 4:
    budget -= budget * 0.75
elif 5 <= people_in_group <= 9:
    budget -= budget * 0.6
elif 10 <= people_in_group <= 24:
    budget -= budget * 0.5
elif 25 <= people_in_group <= 49:
    budget -= budget * 0.4
else:
    budget -= budget * 0.25

if category == "VIP":
    ticket_price = 499.99
elif category == "Normal":
    ticket_price = 249.99

total_tickets = ticket_price * people_in_group
total_end = abs(total_tickets - budget)

if total_tickets <= budget:
    print(f"Yes! You have {total_end:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_end:.2f} leva.")