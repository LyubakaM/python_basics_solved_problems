name = input()
command = input()
counter = 301
curr_points = 0
positive_shots = 0
negative_shot = 0
while command != "Retire":
    points = int(input())
    if command == "Double":
        points *= 2
    elif command == "Triple":
        points *= 3
    if points <= counter:
        positive_shots += 1
        counter -= points
        if counter == 0:
            print(f"{name} won the leg with {positive_shots} shots.")
            break
    else:
        negative_shot += 1
    command = input()
else:
    print(f"{name} retired after {negative_shot} unsuccessful shots.")
