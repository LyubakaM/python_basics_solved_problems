days_to_stay = int(input())
room_type = input()
feedback_positive_or_negative = input()
actual_stay = days_to_stay - 1
one_room = actual_stay * 18.00
apartment = actual_stay * 25.00
president = actual_stay * 35.00
total_cost = 0
if actual_stay < 10:
    if room_type == "room for one person":
        total_cost = one_room
    elif room_type == "apartment":
        total_cost = apartment * 0.7
    elif room_type == "president apartment":
        total_cost = president * 0.9
elif 10 <= actual_stay <= 15:
    if room_type == "room for one person":
        total_cost = one_room
    elif room_type == "apartment":
        total_cost = apartment * 0.65
    elif room_type == "president apartment":
        total_cost = president * 0.85
else:
    if room_type == "room for one person":
        total_cost = one_room
    elif room_type == "apartment":
        total_cost = apartment * 0.5
    elif room_type == "president apartment":
        total_cost = president * 0.8

if feedback_positive_or_negative == "positive":
    total_cost = total_cost + (total_cost * 0.25)
elif feedback_positive_or_negative == "negative":
    total_cost = total_cost - (total_cost * 0.10)
print(f"{total_cost:.2f}")

