chrysanthemum_number = int(input())
roses_number = int(input())
tulips_number = int(input())
season = input()
special_day = input()
c_price = 0
r_price = 0
t_price = 0

if season == "Spring" or season == "Summer":
    c_price = 2.00
    r_price = 4.10
    t_price = 2.50
elif season == "Autumn" or season == "Winter":
    c_price = 3.75
    r_price = 4.50
    t_price = 4.15

if special_day == "Y":
    c_price *= 1.15
    r_price *= 1.15
    t_price *= 1.15
total = chrysanthemum_number * c_price + roses_number * r_price + tulips_number * t_price

if tulips_number > 7 and season == "Spring":
    total *= 0.95
elif roses_number >= 10 and season == "Winter":
    total *= 0.90
if chrysanthemum_number + tulips_number + roses_number > 20:
    total *= 0.80

with_2 = total + 2
print(f"{with_2:.2f}")