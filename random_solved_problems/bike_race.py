junior_bikers = int(input())
senior_bikers = int(input())
track_type = input()
junior_ticket_price = 0
senior_ticket_price = 0


if track_type == "trail":
    junior_ticket_price = 5.5
    senior_ticket_price = 7
elif track_type == "cross-country":
    junior_ticket_price = 8
    senior_ticket_price = 9.50

elif track_type == "downhill":
    junior_ticket_price = 12.25
    senior_ticket_price = 13.75
elif track_type == "road":
    junior_ticket_price = 20
    senior_ticket_price = 21.50

total = junior_ticket_price * junior_bikers + senior_ticket_price * senior_bikers

if junior_bikers + senior_bikers >= 50 and track_type == "cross-country":
    total *= 0.75

expenses = total * 0.05
end = abs(total - expenses)
print(f"{end:.2f}")