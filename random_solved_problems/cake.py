width = int(input())
length = int(input())
cake = length * width
end = False
while cake > 0:
    command = input()
    if command == "STOP":
        end = True
        break
    else:
        while_command = int(command)
        cake -= while_command
diff = abs(cake)
if end:
    print(f"{cake} pieces are left.")
else:
    print(f"No more cake left! You need {diff} pieces more.")

