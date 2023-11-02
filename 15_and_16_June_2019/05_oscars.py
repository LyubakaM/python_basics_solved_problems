act_name = input()
points = float(input())
number = int(input())

nom_points = 1250.5

for i in range(number):
    jury_name = input()
    jury_points = float(input())
    points += len(jury_name) * jury_points / 2

    if points > nom_points:
        print(f"Congratulations, {act_name} got a nominee for leading role with {points:.1f}!")
        break

if points < nom_points:
    print(f"Sorry, {act_name} you need {(nom_points - points):.1f} more!")

