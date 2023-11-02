from math import floor, ceil

shooting_time = int(input())
scenes_number = int(input())
scene_time = int(input())

preparation_time = shooting_time * 0.15
time_for_shooting_scene = scenes_number * scene_time
needed_time = preparation_time + time_for_shooting_scene
diff = abs(needed_time - shooting_time)
diff2 = ceil(diff)


if needed_time <= shooting_time:
    print(f"You managed to finish the movie on time! You have {floor(diff2)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {floor(diff2)} minutes.")