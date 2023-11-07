from sys import maxsize
count = - maxsize  #ZA MIN maham minusa i dolu sum_somm < count


while True:
    command = input()
    if command == "Stop":
        break
    sum_command = int(command)

    if sum_command > count:
        count = sum_command

print(count)
