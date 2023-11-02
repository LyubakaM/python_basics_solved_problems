goals_counter = 0
best_player = ""
before_player = ""
curr_count = 0
player_name = input()
while player_name != "END":
    goals = int(input())
    if goals > goals_counter:
        goals_counter = goals
        best_player = player_name
    if goals >= 10:
        break
    player_name = input()

print(f"{best_player} is the best player!")
if goals_counter >= 3:
    print(f"He has scored {goals_counter} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goals_counter} goals.")