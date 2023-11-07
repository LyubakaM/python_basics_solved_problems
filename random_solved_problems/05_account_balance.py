count = 0
while True:
    command = input()
    if command == "NoMoreMoney":
        break
    current_num = float(command)
    if current_num >= 0:
        count += current_num
        print(f"Increase: {current_num:.2f}")
    else:
        print(f"Invalid operation!")
        break
print(f"Total: {count:.2f}")

