bottles = int(input())
pots_count = 0
dishes_count = 0
days_count = 0
fluid_per_bottle = bottles * 750
end = False
while fluid_per_bottle >= 0:
    command = input()
    if command == "End":
        end = True
        break
    int_command = int(command)
    days_count += 1
    if days_count % 3 == 0:
        fluid_per_bottle -= (int_command * 15)
        pots_count += int_command
    else:
        fluid_per_bottle -= (int_command * 5)
        dishes_count += int_command
diff = abs(fluid_per_bottle)
if end:
    print(f"Detergent was enough!")
    print(f"{dishes_count} dishes and {pots_count} pots were washed.")
    print(f"Leftover detergent {diff} ml.")
else:
    print(f"Not enough detergent, {diff} ml. more necessary!")
