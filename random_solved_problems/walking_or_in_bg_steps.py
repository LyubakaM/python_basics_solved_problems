aim = 10000
steps_count = 0
counter = 0
command = ""
achieved_goal = False
while steps_count < aim:
    command = input()
    if command == "Going home":
        steps_to_home = int(input())
        steps_count += steps_to_home
        break

    steps_count += int(command)

diff = abs(aim - steps_count)
if steps_count >= aim:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff}more steps to reach goal.")
