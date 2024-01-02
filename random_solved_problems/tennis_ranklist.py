from math import floor
tournaments_entered = int(input())
starting_points = int(input())
points_counter = 0
win_counter = 0
for stage in range(1, tournaments_entered + 1):
    reached_stage = input()
    if reached_stage == "W":
        points_counter += 2000
        win_counter += 1
    elif reached_stage == "F":
        points_counter += 1200
    elif reached_stage == "SF":
        points_counter += 720
total_points = points_counter + starting_points
mid = points_counter / tournaments_entered
percent = (win_counter / tournaments_entered) * 100
print(f"Final points: {total_points}")
print(f"Average points: {floor(mid)}")
print(f"{percent:.2f}%")
