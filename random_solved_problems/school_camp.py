season = input()
group_type = input()
students_number = int(input())
days_to_stay = int(input())

price = 0
sport = ""

if group_type == "boys":
    if season == "Winter":
        price = 9.60
        sport = "Judo"
    elif season == "Spring":
        price = 7.20
        sport = "Tennis"
    elif season == "Summer":
        price = 15
        sport = "Football"
elif group_type == "girls":
    if season == "Winter":
        price = 9.60
        sport = "Gymnastics"
    elif season == "Spring":
        price = 7.20
        sport = "Athletics"
    elif season == "Summer":
        price = 15
        sport = "Volleyball"
elif group_type == "mixed":
    if season == "Winter":
        price = 10
        sport = "Ski"
    elif season == "Spring":
        price = 9.50
        sport = "Cycling"
    elif season == "Summer":
        price = 20
        sport = "Swimming"

total = students_number * price * days_to_stay

if students_number >= 50:
    total *= 0.50
elif 20 <= students_number < 50:
    total *= 0.85
elif 10 <= students_number < 20:
    total *= 0.95

print(f"{sport} {total:.2f} lv.")