from math import floor

name = input()
seasons_count = int(input())
episodes_count = int(input())
time_no_commercials = float(input())

time_commercial_per_episode = (time_no_commercials * 0.2)
episode_com = time_commercial_per_episode + time_no_commercials
extra = seasons_count * 10
total = episode_com * episodes_count * seasons_count + extra

print(f"Total time needed to watch the {name} series is {floor(total)} minutes.")
