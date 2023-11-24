season = input()
nights_count = int(input())

apartment = 0
studio = 0

if season == "May" or season == "October":
    studio = nights_count * 50
    apartment = nights_count * 65
    if 7 < nights_count < 14:
        studio = studio - (studio * 0.05)
    elif nights_count > 14:
        studio = studio - (studio * 0.3)
        apartment = apartment - (apartment * 0.1)
elif season == "June" or season == "September":
    studio = nights_count * 75.20
    apartment = nights_count * 68.70
    if nights_count > 14:
        studio = studio - (studio * 0.20)
        apartment = apartment - (apartment * 0.1)
elif season == "July" or season == "August":
    studio = nights_count * 76
    apartment = nights_count * 77
    if nights_count > 14:
        apartment = apartment - (apartment * 0.1)

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")

