visitors_number = int(input())
back_count = 0
chest_count = 0
legs_count = 0
abs_count = 0
protein_count = 0
p_bar__count = 0
workout_percent = 0
protein_percent = 0

for visitor in range(visitors_number):
    activity = input()
    if activity == "Back":
        back_count += 1
    elif activity == "Chest":
        chest_count += 1

    elif activity == "Legs":
        legs_count += 1
    elif activity == "Abs":

        abs_count += 1
    elif activity == "Protein shake":
        protein_count += 1

    elif activity == "Protein bar":
        p_bar__count += 1

workout_total = back_count + chest_count + legs_count + abs_count
protein_total = protein_count + p_bar__count
workout_average = (workout_total / visitors_number) * 100
protein_average = (protein_total / visitors_number) * 100

print(f"{back_count} - back")
print(f"{chest_count} - chest")
print(f"{legs_count} - legs")
print(f"{abs_count} - abs")
print(f"{protein_count} - protein shake")
print(f"{p_bar__count} - protein bar")
print(f"{workout_average:.2f}% - work out")
print(f"{protein_average:.2f}% - protein")


n = int(input())
back = 0
chest = 0
legs = 0
abs_work = 0
protein = 0
shake = 0
work = 0
goods = 0
for _ in range(n):

    pokupka = input()

    if pokupka == "Back":
        back += 1
        work += 1
    elif pokupka == "Chest":
        chest += 1
        work += 1
    elif pokupka == "Legs":
        legs += 1
        work += 1
    elif pokupka == "Abs":
        abs_work += 1
        work += 1
    elif pokupka == "Protein shake":
        shake += 1
        goods += 1
    elif pokupka == "Protein bar":
        protein += 1
        goods += 1
ave_work = work / n * 100
ave_goods = goods / n * 100
print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs_work} - abs")
print(f"{shake} - protein shake")
print(f"{protein} - protein bar")
print(f"{ave_work:.2f}% - work out")
print(f"{ave_goods:.2f}% - protein")

