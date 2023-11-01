tournament_num = int(input())
points = int(input())

tournament_points = 0
win = 0

for _ in range(tournament_num):
    tournament_phase = input()
    if tournament_phase == "W":
        tournament_points += 2000
        win += 1
    elif tournament_phase == "F":
        tournament_points += 1200
    elif tournament_phase == "SF":
        tournament_points += 720

points = points + tournament_points

print(f"Final points: {points}")
print(f"Average points: {tournament_points // tournament_num}")
print(f"{win / tournament_num * 100:.2f}%")

