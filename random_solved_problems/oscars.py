actor = input()
points = float(input())
judges_count_n = int(input())
win_points = False


for judge in range(1, judges_count_n + 1):
    name = input()
    given_points = float(input())
    points += (len(name) * given_points) / 2
    if points > 1250.5:
        win_points = True
        break
diff = abs(1250.5 - points)
if win_points:
    print(f"Congratulations, {actor} got a nominee for leading role with {points:.1f}!")
else:
    print(f"Sorry, {actor} you need {diff:.1f} more!")
