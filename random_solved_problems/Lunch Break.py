from math import ceil

name = input()
episode_time = int(input())
lunch_break = int(input())

lunch_time = ceil(lunch_break / 8)
rest_time = ceil(lunch_break / 4)
time_remaining = lunch_break - lunch_time - rest_time
diff = abs(episode_time - time_remaining)


if time_remaining >= episode_time:
    print(f"You have enough time to watch {name} and left with {diff} minutes free time.")

else:
    print(f"You don't have enough time to watch {name}, you need {diff} more minutes.")
