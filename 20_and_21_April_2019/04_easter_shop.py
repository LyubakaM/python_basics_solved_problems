available_quantity = int(input())
command = input()
counter = 0
while command != "Close":
    curr_sum = int(input())
    if command == "Buy" and curr_sum > available_quantity:
        print(f"Not enough eggs in store!")
        print(f"You can buy only {available_quantity}.")
        break
    if command == "Buy":
        available_quantity -= curr_sum
        counter += curr_sum
    elif command == "Fill":
        available_quantity += curr_sum
    command = input()
else:
    print(f"Store is closed!")
    print(f"{counter} eggs sold.")